# LogAnalsys
This project, you will stretch your SQL database skills. You will get practice interacting with a live database both from the command line and from your code. You will explore a large database with over a million rows. And you will build and refine complex queries and use them to draw business conclusions from data.


PreRequisites:
Python3
Vagrant
VirtualBox
Setup Project:


##Setup Project:
1.nstall Vagrant and VirtualBox
2.Download or Clone fullstack-nanodegree-vm repository.
4.Unzip this file after downloading it. The file inside is called newsdata.sql.
5.Copy the newsdata.sql file and content of this current repository
6.Load the data in local database using the command:
psql -d news -f newsdata.sql
7.Use psql -d news to connect to database

##View article_view
create view article_view as select title,author,count(*) as views from articles,log where
log.path like concat('%',articles.slug) group by articles.title,articles.author
order by views desc;

##View error_log_view
create view error_log_view as select date(time),round(100.0*sum(case log.status when '200 OK'
then 0 else 1 end)/count(log.status),2) as "Percent Error" from log group by date(time)
order by "Percent Error" desc;

##Running the queries:
 From the vagrant directory inside the virtual machine,run logs.py using:
 $ python3 logs.py
