#!/usr/bin/env python3

import logging
import argparse

import rpToolServe

if __name__ == "__main__":
    parser = argparse.ArgumentParser('Generate the sink from a model SBML by specifying the compartment')
    parser.add_argument('-inSBML', type=str)
    parser.add_argument('-outputSink', type=str)
    parser.add_argument('-compartment_id', type=str, default='MNXC3')
    #TODO: check that the compartmentId exists and return an error if not. Idea: print the list of available compartments if error is found
    params = parser.parse_args()
    rpToolServe.main(params.inSBML, params.outputSink, params.compartment_id)
    exit(0)
