import argparse
import os


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-b", "--board_grid", type=int, help="board_length")
    parser.add_argument("-u", "--unit_grid", type=int, help="unit_length")
    parser.add_argument("--unit_n", type=int, help="unit numbers")
    parser.add_argument("--positions", type=str)
    parser.add_argument("-o", "--outdir", type=str, default="example_dir")
    parser.add_argument("--file_name", type=str, default="example")
    args = parser.parse_args()
    if args.board_grid % args.unit_grid != 0:
        print("mod error")
        exit()
    positions = args.positions.split(' ')  # --positions 1 4
    if len(positions) != args.unit_n:
        exit()
    else:
        for pos in positions:
            if int(pos) >= int(args.board_grid/args.unit_grid) ** 2:
                print("too large, error")
                print(pos, int(args.board_grid/args.unit_grid) ** 2)
                exit()
    if not os.path.exists(args.outdir):
        os.makedirs(args.outdir)
    f = open('./%s/%s.mat' % (args.outdir, args.file_name), 'w')
    f.close()
    f2 = open('./%s/%s.jpg' % (args.outdir, args.file_name), 'w')
    f2.close()


if __name__ == "__main__":
    main()
