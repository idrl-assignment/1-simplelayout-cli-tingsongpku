import argparse
import os


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-b", "--board_grid", type=int, help="board_length")
    parser.add_argument("-u", "--unit_grid", type=int, help="unit_length")
    parser.add_argument("--unit_n", type=int, help="unit numbers")
    parser.add_argument("--positions", type=int)
    parser.add_argument("-o", "--outdir", type=str, default="example_dir")
    parser.add_argument("--file_name", type=str, default="example")
    args = parser.parse_args()
    if args.board_grid % args.unit_grid != 0:
        print("mod error")
        exit()
    if args.positions != args.unit_n:
        print("#positions != #unit_n, error")
        exit()
    if args.positions >= int(args.board_grid/args.unit_grid) ^ 2:
        print("too large, error")
        exit()
    #if args.outdir not in os.listdir("."):无法遍历深层目录，os.listdir只能读取一层，读取深层需要结合os.walk
    if not os.path.exists(args.outdir):
        os.makedirs(args.outdir)
    f = open('./%s/%s.mat' % (args.outdir, args.file_name), 'w')
    f.close()
    f2 = open('./%s/%s.jpg' % (args.outdir, args.file_name), 'w')
    f2.close()


if __name__ == "__main__":
    main()
