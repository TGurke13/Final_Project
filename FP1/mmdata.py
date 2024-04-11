import pandas as pd

# Load the March Madness data 
ratings = pd.read_csv('C:\\Users\\thoma\\OneDrive\\Desktop\\School-Stuff\\Final_Project\\MM_CSV\\538 Ratings.csv')
coach_results = pd.read_csv('C:\\Users\\thoma\\OneDrive\\Desktop\\School-Stuff\\Final_Project\\MM_CSV\\Coach Results.csv')
team_results = pd.read_csv('C:\\Users\\thoma\\OneDrive\\Desktop\\School-Stuff\\Final_Project\\MM_CSV\\Team Results.csv')
tournament_matchups = pd.read_csv('C:\\Users\\thoma\\OneDrive\\Desktop\\School-Stuff\\Final_Project\\MM_CSV\\Tournament Matchups.csv')
team_resume = pd.read_csv('C:\\Users\\thoma\\OneDrive\\Desktop\\School-Stuff\\Final_Project\\MM_CSV\\Resumes.csv')
conference_results = pd.read_csv('C:\\Users\\thoma\\OneDrive\\Desktop\\School-Stuff\\Final_Project\\MM_CSV\\Conference Results.csv')
conference_away_neutral = pd.read_csv('C:\\Users\\thoma\\OneDrive\\Desktop\\School-Stuff\\Final_Project\\MM_CSV\\Conference Stats Away Neutral.csv')
conference_away = pd.read_csv('C:\\Users\\thoma\\OneDrive\\Desktop\\School-Stuff\\Final_Project\\MM_CSV\\Conference Stats Away.csv')
conference_home = pd.read_csv('C:\\Users\\thoma\\OneDrive\\Desktop\\School-Stuff\\Final_Project\\MM_CSV\\Conference Stats Home.csv')
conference_neutral = pd.read_csv('C:\\Users\\thoma\\OneDrive\\Desktop\\School-Stuff\\Final_Project\\MM_CSV\\Conference Stats Neutral.csv')
conference_stats = pd.read_csv('C:\\Users\\thoma\\OneDrive\\Desktop\\School-Stuff\\Final_Project\\MM_CSV\\Conference Stats.csv')
num_of_upsets = pd.read_csv('C:\\Users\\thoma\\OneDrive\\Desktop\\School-Stuff\\Final_Project\\MM_CSV\\Upset Count.csv')
# Not 100% sure what this is
heat_check = pd.read_csv('C:\\Users\\thoma\\OneDrive\\Desktop\\School-Stuff\\Final_Project\\MM_CSV\\Heat Check Tournament Index.csv')