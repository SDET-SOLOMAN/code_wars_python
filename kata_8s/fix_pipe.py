# Practice
# Complete challenging Kata to earn honor and ranks. Re-train to hone technique
# Freestyle Sparring
# Take turns remixing and refactoring others code through Kumite
# CAREER
# Opportunities
# Find your next career challenge – powered by Qualified Jobs
# COMMUNITY
# Leaderboards
# Achieve honor and move up the global leaderboards
# Chat
# Join our Discord server and chat with your fellow code warriors
# Discussions
# View our Github Discussions board to discuss general Codewars topics
# ABOUT
# Docs
# Learn about all of the different aspects of Codewars
# El Coder Avatar
# 4 kyu
# 1,065
# 8 kyu
# Lario and Muigi Pipe Problem
#
# 34810992% of 3,34110,065 of 30,445LiamSorta1 Issue Reported
#  Python
# 3.11
# VIM
# EMACS
# Instructions
# Output
# Issue
#
# Looks like some hoodlum plumber and his brother has been running around and damaging your stages again.
#
# The pipes connecting your level's stages together need to be fixed before you receive any more complaints.
#
# The pipes are correct when each pipe after the first is 1 more than the previous one.
#
# Task
#
# Given a list of unique numbers sorted in ascending order, return a new list so that the values increment
# by 1 for each index from the minimum value up to the maximum value (both included).
#
# Example
#
# Input:  1,3,5,6,7,8 Output: 1,2,3,4,5,6,7,8

def pipe_fix(nums):
    return list(map(lambda x: x, range(nums[0], nums[-1] + 1)))