import argparse
import os
from . import auto_mkdir, import_task

parser = argparse.ArgumentParser()

parser.add_argument("--model_name", type=str,
                    help="""Name of the model.""")

parser.add_argument("--source_path", type=str,
                    help="""Path to source file.""")

parser.add_argument("--model_path", type=str,
                    help="""Path to model files.""")

parser.add_argument("--config_path", type=str,
                    help="""Path to config file.""")

parser.add_argument("--batch_size", type=int, default=5,
                    help="""Batch size of beam search.""")

parser.add_argument("--beam_size", type=int, default=5,
                    help="""Beam size.""")

parser.add_argument("--saveto", type=str,
                    help="""Result prefix.""")

parser.add_argument("--keep_n", type=int, default=-1,
                    help="""To keep how many results. This number should not exceed beam size.""")

parser.add_argument("--use_gpu", action="store_true")

parser.add_argument("--max_steps", type=int, default=150,
                    help="""Max steps of decoding. Default is 150.""")

parser.add_argument("--alpha", type=float, default=-1.0,
                    help="""Factor to do length penalty. Negative value means close length penalty.""")

parser.add_argument("--reranking", action="store_true", help="Whether use reconstructive reranking")

parser.add_argument("--beta", type=float, default=0.0,
                    help="""Factor for weighting decoding LM score.""")

parser.add_argument("--gamma", type=float, default=0.0,
                    help="""Factor for weighting reconstructive reranking LM score.""")

parser.add_argument("--src_lang", type=str, default="src",
                    choices=["src", "tgt"],
                    help="""Source langauge.""")

parser.add_argument("--task", type=str, default="baseline",
                    help="""Choose to run which task.""")


def run(**kwargs):
    args = parser.parse_args()

    # Modify some options.
    for k, v in kwargs.items():
        setattr(args, k, v)

    auto_mkdir(os.path.dirname(args.saveto))

    task = import_task(args.task)
    task.translate(args)


if __name__ == '__main__':
    run()