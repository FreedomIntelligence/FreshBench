

### test if can request one question from goodjudge

```
cd fresh_eval
cd sr
cd goodjudge
python request_one_question.py
```

you would see this

```Question,Started_time,Closed_time,Challenges_list,Tags_list,Description,Possible_Answers_dict
What percentage of the vote will Nikki Haley receive in the 2024 Michigan Republican presidential primary?,"Feb 02, 2024 06:00PM UTC","Feb 27, 2024 08:01AM UTC","['2024 US Election Challenge', 'In the News 2024']","['Leader Entry/Exit', 'US Politics', 'Elections and Referenda']","As of the end of January 2024, Nikki Haley was the last major challenger to Donald Trump for the GOP presidential nomination (Politico, Newsweek). The Michigan Republican primary is scheduled for 27 February 2024 (270 to Win).","{'Less than 10.0%': {'Correct?': False, 'Final Crowd Forecast': '6%'}, 'At least 10.0%, but less than 20.0%': {'Correct?': False, 'Final Crowd Forecast': '23%'}, 'At least 20.0%, but less than 30.0%': {'Correct?': True, 'Final Crowd Forecast': '62%'}, 'At least 30.0%, but less than 40.0%': {'Correct?': False, 'Final Crowd Forecast': '8%'}, '40.0% or more': {'Correct?': False, 'Final Crowd Forecast': '1%'}}"```


### then 


