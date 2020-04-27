  create table tasks (
      id integer not null,
      name varchar(40) not null,
      unique(id)
  );

  create table reports (
      id integer not null,
      task_id integer not null,
      candidate varchar(40) not null,
      score integer not null,
      unique(id)
  );
  
insert into tasks values (101, 'MinDist');
insert into tasks values (123, 'Equi');
insert into tasks values (142, 'Median');
insert into tasks values (300, 'Tricoloring');
insert into reports values (13, 101, 'John Smith', 100);
insert into reports values (24, 123, 'Delaney Lloyd', 34);
insert into reports values (37, 300, 'Monroe Jimenez', 50);
insert into reports values (49, 101, 'Stanley Price', 45);
insert into reports values (51, 142, 'Tanner Sears', 37);
insert into reports values (68, 142, 'Lara Fraser', 3);
insert into reports values (83, 300, 'Tanner Sears', 0);

create table temp(

task_id integer not null,
avg_score float not null

);

insert into temp
select task_id, avg(score) 
from reports
group by task_id;

SELECT a.id as task_id, a.name as task_name,
case when b.avg_score < 30 then 'hard'
when b.avg_score >= 30 and b.avg_score < 60 then 'middle'
when b.avg_score >= 60 then 'easy'
end as difficulty
FROM tasks a
JOIN temp b
ON a.id = b.task_id;