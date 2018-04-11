import argparse
import simpleai.search as ss

def build_arg_parser():
    parser = argparse.ArgumentParser(description='Creates the input string using the greedy algorithm')
    parser.add_argument("--input-string", dest="input_string",required=True,help="Input string")
    parser.add_argument("--initial-state", dest="initial_state",required=False,default='', help="Starting point for the search")
    return parser


class CustomProblem(ss.SearchProblem):


    def set_target(self, target_string):

        self.target_string = target_string
    # Check the current state and take the right action
    def actions(self, cur_state):
        if len(cur_state) < len(self.target_string):

            alphabets = 'abcdefghijklmnopqrstuvwxyz'
            return list(alphabets + ' ' + alphabets.upper())
        else:
            return []
