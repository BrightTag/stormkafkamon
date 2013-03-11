#!/usr/bin/env python

import argparse
import sys
from zkclient import *

def display(topics, brokers):
    print 'Partition\t\tEarliest Offset\t\tLatest Offset\t\tSpout\t\t\tCurrent Offset\t\tDelta (bytes)'
    print '===================================================================' * 2
    for t in topics:
        for i in range(int(t.num_partitions)):
            print '%s:%s:%d' % (t.broker, t.topic, i)
            print '-------------------------------------------------------------------' * 2

######################################################################

def read_args():
    parser = argparse.ArgumentParser(
        description='Show complete state of Storm-Kafka consumers')
    parser.add_argument('--zserver', default='localhost',
        help='Zookeeper host (default: localhost)')
    parser.add_argument('--zport', type=int, default=2181,
        help='Zookeeper port (default: 2181)')
    parser.add_argument('--topic', type=str, default='test',
        help='Kafka topic (default: test)')
    parser.add_argument('--topology', type=str, required=True,
        help='Storm Topology')
    return parser.parse_args()

def main():
    options = read_args()

    zc = ZkClient(options.zserver, options.zport)

    display(zc.topics(), zc.brokers())

if __name__ == '__main__':
    sys.exit(main())
