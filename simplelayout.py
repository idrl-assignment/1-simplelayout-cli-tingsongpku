import argparse
import os


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-b", "--board_grid", type=int, help="the length of the board")
    parser.add_argument("-u", "--unit_grid", type=int, help="the length of the unit")
    parser.add_argument("--unit_n", type=int, help="unit numbers")
    parser.add_argument("--positions", type=int)
    parser.add_argument("-o", "--outdir", type=str, default="example_dir")
    parser.add_argument("--filename", type=str, default="example")
    args = parser.parse_args()
    if args.board_grid % args.unit_grid !=0:
        print("mod error")
        exit()
    if args.positions != args.unit_grid:
        print("#positions != #unit_grid, error")
        exit()
    if args.positions >= (args.board_grid/args.unit_grid)^2:
        print("too large, error")
        exit()
    if args.outdir not in os.listdir("."):
        os.makedirs(args.outdir)
        f=open('./%s/%s.mat'% (args.outdir, args.filename), 'w')
        f.close()
        f2=open('./%s/%s.jpg'% (args.outdir, args.filename), 'w')
        f2.close()


if __name__ == "__main__":
    main()
