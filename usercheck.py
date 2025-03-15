
import argparse
import urllib.request
import requests
import json

parser = argparse.ArgumentParser()
parser.add_argument("-c", "--check", nargs=1, help="Add a task to the list")
args = parser.parse_args()



def checkuseractivity(username):
    
    url = f"https://api.github.com/users/{username}/events"
    response = requests.get(url, timeout=10)
   
    if response.status_code == 200:
        event = response.json()
       

        latest_events = event

        print(f"Latest events for [bold green]{username}[/bold green]:")

        for event in latest_events:
            
            if event['type'] == 'IssueCommentEvent':
                print(f"commented on issue {event['payload']['issue']['number']}")
            elif event['type'] == 'PushEvent':
               print(f"pushed to {event['repo']['name']}")
            elif event['type'] == 'IssuesEvent':
               print(f" created issue {event['payload']['issue']['number']}")
            elif event['type'] == 'WatchEvent':
                print(f"starred {event['repo']['name']}")
            elif event['type'] == 'PullRequestEvent':
                print(f"created pull request {event['payload']['pull_request']['number']}")
            elif event['type'] == 'PullRequestReviewEvent':
                print(f" reviewed pull request {event['payload']['pull_request']['number']}")
            elif event['type'] == 'PullRequestReviewCommentEvent':
                print(f" commented on pull request {event['payload']['pull_request']['number']}")
            elif event['type'] == 'CreateEvent':
                print(f" created {event['payload']['ref_type']} {event['payload']['ref']}")
            else:
                print(f"{event['type']}")
    else:
        print(f"Error fetching events for {username}: {response.status_code}")

    
    
    
if args.check:
    checkuseractivity(args.check[0])





