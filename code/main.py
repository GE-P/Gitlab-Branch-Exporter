# Created by: Gerhard Eibl
# Creation date: 07/06/2022
# Modification date: 07/06/2022
# Version: 0.1a
# Name: Git_Branch_Unifier --
""" This program serves to export branches to separate folders and merge all branches into master """
# -------------------------------------------------------------------------------------------------------------
import os
import shutil
import subprocess

source_path = 'PATH01'
source_path_2 = 'PATH02'
command = "git branch -r --sort=-committerdate"
branch_list = subprocess.check_output(command, cwd=source_path).decode().split('\n')
output = open('branches_list.txt', 'w')
folder_to_remove = os.listdir(source_path_2)
i = 1
branch_dico = {}

for folder in folder_to_remove:
    path_rm = source_path_2 + '/' + folder
    print(path_rm)
    shutil.rmtree(path_rm)

for branch in branch_list:
    split_branches = branch.split('/')

    if branch != '  origin/HEAD -> origin/master' and branch != "" and branch != '  origin/master':

        if split_branches[1] not in branch_dico:
            branch_dico[split_branches[1]] = i

        print(branch)
        print(split_branches[1])
        print(split_branches[1], file=output)

        checkout_command = "git checkout " + split_branches[1]
        checkout = subprocess.Popen(checkout_command, cwd=source_path)
        checkout.wait()

        files = os.listdir(source_path)
        destination_path = source_path_2 + "/" + str(i) + "_" + split_branches[1]
        shutil.copytree(source_path, destination_path, ignore=shutil.ignore_patterns(".git"))
        print(files)
        i += 1

    checkout_command = "git checkout master"
    checkout = subprocess.Popen(checkout_command, cwd=source_path)
    checkout.wait()

# i += 1
# branch_dico["Original_folder"] = i
# i = 1
# for branch in branch_list:
#
#     # dico_file = {}
#     split_branches = branch.split('/')
#
#     if branch != '  origin/HEAD -> origin/master' and branch != "" and branch != '  origin/master':
#
#         client_config_files = os.listdir(source_path_2 + "/" + str(i) + "_" + split_branches[1])
#
#         # for files in client_config_files:
#         #     i += 1
#         #     if files not in dico_file:
#         #         dico_file[files] = i
#         #
#         # print(dico_file)
#         print(split_branches[1])
#
#         destination_path2 = source_path + "/" + str(i) + "_" + split_branches[1]
#
#         checkout_command_master = "git checkout master"
#         checkout = subprocess.Popen(checkout_command_master, cwd=source_path)
#         checkout.wait()
#         # merge_command = "git merge " + split_branches[1]
#         # merge = subprocess.Popen(merge_command, cwd=source_path)
#         # merge.wait(3)
#         shutil.copytree(source_path_2 + "/" + str(i) + "_" + split_branches[1], destination_path2,
#                         ignore=shutil.ignore_patterns(
#             ".git"))
#
#         i += 1
#
#         # merge_command = "git merge " + split_branches[1]
#         # merge = subprocess.Popen(merge_command, cwd=source_path)
#         # merge.wait(3)
#
#         # files_to_remove = os.listdir(source_path)
#         # for file in files_to_remove:
#         #     if file not in branch_dico and file != ".git" and file != "CHANGELOG":
#         #         if os.path.isfile(source_path + "/" + file) is True:
#         #             os.remove(source_path + "/" + file)
#         #         elif os.path.isdir(source_path + "/" + file):
#         #             shutil.rmtree(source_path + "/" + file)
#
#         # for file in files_to_remove:
#         #     if file in dico_file and file != ".git" and file != "CHANGELOG":
#         #         if os.path.isfile(source_path + "/" + file) is True:
#         #             shutil.move(source_path + "/" + file, source_path + "/" + split_branches[1] + "/" + file)
#         #         elif os.path.isdir(source_path + "/" + file) is True:
#         #             shutil.move(source_path + "/" + file, source_path + "/" + split_branches[1] + "/" + file)
#
#         # add_command = "git add ."
#         # add = subprocess.Popen(add_command, cwd=source_path)
#         # add.wait(3)
#         #
#         # commit_command = 'git commit -m "merge: merging branch to master"'
#         # commit = subprocess.Popen(commit_command, cwd=source_path)
#         # commit.wait(3)
#
#         # add_command = "git add ."
#         # add = subprocess.Popen(add_command, cwd=source_path)
#         # add.wait(3)
#
#         # remove_path = source_path_2 + "/" + split_branches[1]
#         # files_to_remove = os.listdir(remove_path)
#         # for file in files_to_remove:
#         #     if os.path.isfile(remove_path + "/" + file) is True:
#         #         os.remove(source_path + "/" + file)
#         #     elif os.path.isdir(remove_path + "/" + file):
#         #         shutil.rmtree(source_path + "/" + file)
#
#         # push_command = "git push"
#         # push = subprocess.Popen(push_command, cwd=source_path)
#         # push.wait(3)
# i = 1
# j = 1
# for branch in branch_list:
#
#     dico_file = {}
#     split_branches = branch.split('/')
#
#     if branch != '  origin/HEAD -> origin/master' and branch != "" and branch != '  origin/master':
#
#         client_config_files = os.listdir(source_path_2 + "/" + str(i) + "_" + split_branches[1])
#
#         for files in client_config_files:
#             j += 1
#             if files not in dico_file:
#                 dico_file[files] = j
#
#         print(dico_file)
#         print(split_branches[1])
#
#         checkout_command_master = "git checkout master"
#         checkout = subprocess.Popen(checkout_command_master, cwd=source_path)
#         checkout.wait()
#
#         merge_command = "git merge " + split_branches[1]
#         merge = subprocess.Popen(merge_command, cwd=source_path)
#         merge.wait()
#
#         files_to_remove = os.listdir(source_path)
#
#         for file in files_to_remove:
#             if file in dico_file and file != ".git" and file != "CHANGELOG":
#                 if os.path.isfile(source_path + "/" + file) is True:
#                     shutil.move(source_path + "/" + file, source_path + "/" + str(i) + "_" + split_branches[1] + "/" + file)
#                 elif os.path.isdir(source_path + "/" + file) is True:
#                     shutil.move(source_path + "/" + file, source_path + "/" + str(i) + "_" + split_branches[1] + "/" + file)
#
#         add_command = "git add ."
#         add = subprocess.Popen(add_command, cwd=source_path)
#         add.wait()
#
#         commit_command = 'git commit -m "merge: merging branch to master"'
#         commit = subprocess.Popen(commit_command, cwd=source_path)
#         commit.wait()
#
#         i += 1

######################################################## - Old usage code :

# destination_path2 = source_path + "/" + "merge_branch"
# checkout_command_master = "git checkout master"
# checkout = subprocess.Popen(checkout_command_master, cwd=source_path)
# checkout.wait()
# merge_command = "git merge " + "merge_branch"
# merge = subprocess.Popen(merge_command, cwd=source_path)
# merge.wait()
# # add_command = "git add ."
# # add = subprocess.Popen(add_command, cwd=source_path)
# # add.wait()
# # commit_command = 'git commit -m "merge: merge_branch to master"'
# # commit = subprocess.Popen(commit_command, cwd=source_path)
# # commit.wait()
# push_command = "git push"
# push = subprocess.Popen(push_command, cwd=source_path)
# push.wait()
# shutil.copytree(source_path, destination_path2, ignore=shutil.ignore_patterns(".git"))


