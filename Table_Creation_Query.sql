CREATE TABLE [Student] (
  [Roll] varchar(20) PRIMARY KEY,
  [Name] varchar(100),
  [Gender] varchar(10),
  [Email] varchar(20),
  [Phone] varchar(10),
  [MotherName] varchar(10),
  [Fathername] varchar(100),
  [YearOfStudy] integer,
  [BranchId] integer,
  [YearOfGraduation] integer,
  [Caste] varchar(5)
)
GO

CREATE TABLE [Branch] (
  [Branchid] integer PRIMARY KEY,
  [BranchName] nvarchar(255)
)
GO

ALTER TABLE [Student] ADD FOREIGN KEY ([BranchId]) REFERENCES [Branch] ([Branchid])
GO
