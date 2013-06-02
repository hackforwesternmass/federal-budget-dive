create table agency (
    account_seq int,
    account_code varchar,
    account_name varchar
    );

create table bureau (
    agency_seq int,
    bureau_code varchar,
    bureau_name varchar
    );

create table account (
    account_seq int,
    bureau_code varchar,
    treasury_code varchar,
    account_name varchar,
    account_deleted varchar
    );

create table schedule (
    schedule_seq int,
    agency_seq int,
    bureau_code varchar,
    treasury_id varchar,
    schedule_code varchar,
    schedule_treasury_id varchar,
    schedule_name varchar,
    col3_head,
    col4_head,
    col5_head
    );

create table tables (
    schedule_seq int,
    row_num int,
    stub_hierarchy int,
    col1 varchar,
    col2 varchar,
    col3 varchar,
    col4 varchar,
    col5 varchar
    );

.mode csv
.import agency.csv agency
.import bureau.csv bureau
.import account.csv account
.import schedule.csv schedule
.import tables.csv tables
