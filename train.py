import os
os.environ["CUDA_VISIBLE_DEVICES"] = "0"
from pprint import pprint
from config.config import parser
from dataset.data_module import DataModule
from lightning_tools.callbacks import add_callbacks
from models.LLM_RG4 import LLM_RG4
from lightning.pytorch import seed_everything
import lightning.pytorch as pl
import torch


def train(args):
    dm = DataModule(args)
    callbacks = add_callbacks(args)
    print('start train')

    trainer = pl.Trainer(
        devices=args.devices,
        num_nodes=args.num_nodes,
        strategy='auto',
        accelerator=args.accelerator,
        precision=args.precision,
        val_check_interval = args.val_check_interval,
        limit_val_batches = args.limit_val_batches,
        max_epochs = args.max_epochs,
        num_sanity_val_steps = args.num_sanity_val_steps,
        accumulate_grad_batches=args.accumulate_grad_batches,
        callbacks=callbacks["callbacks"],
        logger=callbacks["loggers"]
    )

    model = LLM_RG4(args)

    if args.test:
        trainer.test(model, datamodule=dm)
    elif args.validate:
        trainer.validate(model, datamodule=dm)
    else:
        trainer.fit(model , datamodule=dm)


def main():
    args = parser.parse_args()
    os.makedirs(args.savedmodel_path, exist_ok=True)
    pprint(vars(args))
    seed_everything(42, workers=True)
    train(args)

if __name__ == '__main__':
    main()
    print('success')
