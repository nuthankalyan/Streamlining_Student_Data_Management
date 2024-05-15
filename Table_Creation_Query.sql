CREATE TABLE [Student] (
  [Roll] varchar(20) PRIMARY KEY,
  [Name] varchar(100),
  [Gender] varchar(10),
  [Email] varchar(20),
  [Phone] varchar(10),
  [MotherName] varchar(10),
  [Fathername] varchar(100),
  [YearOfStudy] integer,
  [YearOfGraduation] integer,
  [Caste] varchar(5),
  [BranchName] varchar(10)
)
GO

CREATE TABLE [Branch] (
  [Branchid] integer,
  [BranchName] nvarchar(255) PRIMARY KEY
)
GO

ALTER TABLE [Student] ADD FOREIGN KEY ([BranchName]) REFERENCES [Branch] ([BranchName])
GO
