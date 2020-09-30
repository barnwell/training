import os
import random
# version_name = input("Test Plan Version: ") or "default"
version_name = "baseline"
random_seed = 'clinc'
# version_name = "refreshed"
# random_seed = 'v75'
random.seed(random_seed)
aivc_tests_directory = "aivc-tests" + os.sep + version_name
#name of file goes here
chatette_plans = [
    #'clf_prevention_method_start.chatette',
    #'clf_subscription_start.chatette',
    #'clf_activity_start.chatette',
    #'clf_help_desk_start.chatette',
    #'clf_social_distance_start.chatette',
    'clf_statistics_start.chatette',
    'clf_unsubscribe_start.chatette',
    'clf_risk_start.chatette',

]
def generate_chatette_tests():
    if not os.path.isdir(aivc_tests_directory):
        os.mkdir(aivc_tests_directory)
    for chatette_plan in chatette_plans:
        output_filename = chatette_plan.replace('.chatette', '') + '.txt'
        os.system(
            'python3 -m chatette -f ' +
            ' -s ' + random_seed +
            #adapter goes here
            ' -a rasamd chatette-tests' + os.sep + chatette_plan +
            ' -o ' + aivc_tests_directory + os.sep + chatette_plan
        )
        os.system(
            'mv ' + aivc_tests_directory + os.sep + chatette_plan + os.sep + 'train' + os.sep + 'output.md' +
            '   ' + aivc_tests_directory + os.sep + output_filename
        )
        os.system(
            'rm -rf ' + aivc_tests_directory + os.sep + chatette_plan
        )

generate_chatette_tests()

#cd /mnt/c/users/KVHoy/pycharmprojects/chatette