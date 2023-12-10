import requests
import sys
import json

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def main():
    # Remplacez ces valeurs par les vôtres
    token = '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'
    username = 'bricemab'

    repoName = input("Enter repository name: ").strip()
    if repoName == "":
        exit_program("No repository name entry")
    isPublicAsw = input("Public repository (default yes)").strip()
    isPublic = isPublicAsw == "" or isPublicAsw.lower() == "yes" or isPublicAsw.lower() == "y"
    # Créez un nouveau dépôt
    url = f'https://api.github.com/user/repos'
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/json',
    }
    data = {
        'name': repoName,
        'private': not isPublic,  # Changez à True si vous voulez un dépôt privé
    }
    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 201:
        print(f'Repository create with success')
        print(f"git clone https://github.com/{username}/{repoName}")
    else:
        error_response = json.loads(response.text)
        error_message = error_response['message']
        for error in error_response['errors']:
            if 'message' in error:
                error_message = error['message']
                break   
        exit_program(error_message)

def exit_program(error):
    print(f"{bcolors.FAIL}{error}{bcolors.ENDC}")
    sys.exit(0)

main()