-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.

-- Modify this code to update the DB schema diagram.
-- To reset the sample schema, replace everything with
-- two dots ('..' - without quotes).

CREATE TABLE "User" (
    "UserID" int   NOT NULL,
    "Username" string   NOT NULL,
    "FirstName" string   NOT NULL,
    "LastName" string   NOT NULL,
    "Email" email   NOT NULL,
    "Password" string   NOT NULL,
    CONSTRAINT "pk_User" PRIMARY KEY (
        "UserID"
     ),
    CONSTRAINT "uc_User_Username" UNIQUE (
        "Username"
    ),
    CONSTRAINT "uc_User_Email" UNIQUE (
        "Email"
    )
);

CREATE TABLE "Job" (
    "JobID" int   NOT NULL,
    "JobTitle" string   NOT NULL,
    "Location" string   NOT NULL,
    "StartYear" integer   NOT NULL,
    "DayRate" money   NOT NULL,
    "UserID" int   NOT NULL,
    CONSTRAINT "pk_Job" PRIMARY KEY (
        "JobID"
     )
);

ALTER TABLE "Job" ADD CONSTRAINT "fk_Job_UserID" FOREIGN KEY("UserID")
REFERENCES "User" ("UserID");

