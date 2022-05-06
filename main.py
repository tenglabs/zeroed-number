from zeroed import generate_list, sorted_iteration, traversing_array, xor_array
import argparse


parser = argparse.ArgumentParser(description='Add some integers.')

parser.add_argument('max', type=int, help='Maximum range')
parser.add_argument('operation', help='operation')

args = parser.parse_args()
print(f'Maximum Number is {args.max} ' )


gl = generate_list(max_num=args.max)

if args.operation == 'sorted_iter':
    
    sorted_iteration(a=gl)

elif args.operation == 'traversing_array':

    traversing_array(a=gl)

elif args.operation == 'xor':

    xor_array(a=gl)