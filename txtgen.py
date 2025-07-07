#!/usr/bin/env python3
import argparse

def generate_text(count):
    return "lorem ipsum " * count

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, default=1)
    args = parser.parse_args()
    print(generate_text(args.count))

if __name__ == "__main__":
    main()
