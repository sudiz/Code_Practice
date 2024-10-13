select team_id,team_name, 
sum(case when host_goals=guest_goals then 1
        when team_id=host_team and host_goals>guest_goals then 3
        when team_id=host_team and host_goals<guest_goals then 0
        when team_id=guest_team and host_goals<guest_goals then 3
        else 0 
        end
) as num_points
from Teams left join Matches
on Teams.team_id=Matches.host_team
or Teams.team_id=Matches.guest_team
group by team_id,team_name
order by num_points desc,team_id
