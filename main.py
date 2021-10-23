import os
from utils.get_args import Args
from utils.utils import fix_random_seed, timeit, write_csv
from data_loader.data_generator import DataGenerator
from models.model_builder import ModelBuilder
from trainers.trainer_maker import TrainerMaker


@timeit
def main():
    args_class = Args()
    args = args_class.args

    for args.subject in args.target_subject:
        args_class.preprocess()
        args_class.print_info()

        # Fix random seed
        if args.seed:
            fix_random_seed(args)

        # Load data
        data = DataGenerator(args)

        # Build model
        model = ModelBuilder(args).model

        # Make Trainer
        trainer = TrainerMaker(args, model, data).trainer

        if args.mode == 'train':
            trainer.train()
        elif args.get_prediction:
            trainer.get_prediction()
        elif args.evaluation:
            trainer.evaluation()
        else:
            trainer.test()

    if args.evaluation:
        write_csv(os.path.join(args.base_load_path, "prediction.csv"), args.acc_list)


if __name__ == '__main__':
    main()
