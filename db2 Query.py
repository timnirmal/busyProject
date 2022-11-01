new_string = """-- AMCWarrDet definition

-- Drop table

-- DROP TABLE AMCWarrDet;

CREATE TABLE AMCWarrDet (
	VchCode integer DEFAULT 0,
	SrNo smallint DEFAULT 0,
	Rectype smallint DEFAULT 0,
	Date timestamp ,
	VchNo text,
	RefNo text,
	ItemSerialNo text,
	MasterCode1 integer DEFAULT 0,
	MasterCode2 integer DEFAULT 0,
	Value1 float DEFAULT 0,
	CM1 integer DEFAULT 0,
	Narration text,
	ContEndDate timestamp ,
	I1 smallint DEFAULT 0,
	Status smallint DEFAULT 0
);
CREATE INDEX AMCWARRDET_01 ON AMCWarrDet (MasterCode1);
CREATE INDEX AMCWARRDET_02 ON AMCWarrDet (MasterCode2);
CREATE INDEX AMCWARRDET_03 ON AMCWarrDet (ItemSerialNo);
CREATE INDEX AMCWARRDET_04 ON AMCWarrDet (RefNo);
CREATE INDEX AMCWARRDET_05 ON AMCWarrDet (ContEndDate);
CREATE INDEX AMCWARRDET_06 ON AMCWarrDet (VchNo);
CREATE INDEX AMCWARRDET_07 ON AMCWarrDet (Status);



-- BillingDet definition

-- Drop table

-- DROP TABLE BillingDet;

CREATE TABLE BillingDet (
	VchCode integer DEFAULT 0,
	PartyName text,
	Address1 text,
	Address2 text,
	Address3 text,
	Address4 text,
	STNo text,
	CSTNo text,
	ECCCode text,
	ExciseRegNo text,
	PLANo text,
	Range text,
	Division text,
	Collectorate text,
	MobileNo text,
	Email text,
	DrugLicenceNo1 text,
	DrugLicenceNo2 text,
	ITPAN text
);
CREATE INDEX BILLINGDET_01 ON BillingDet (VchCode);
CREATE INDEX BILLINGDET_02 ON BillingDet (PartyName);
CREATE INDEX BILLINGDET_03 ON BillingDet (MobileNo);
CREATE INDEX BILLINGDET_04 ON BillingDet (Email);




-- BRSOpBal definition

-- Drop table

-- DROP TABLE BRSOpBal;

CREATE TABLE BRSOpBal (
	SrNo smallint DEFAULT 0,
	MasterCode1 integer DEFAULT 0,
	MasterCode2 integer DEFAULT 0,
	OpAmt float DEFAULT 0,
	Type smallint DEFAULT 0,
	ShortNar text,
	EntryDate timestamp ,
	ClrDate timestamp ,
	OldVchCode integer DEFAULT 0,
	VchNo text
);
CREATE INDEX BRSOPBAL_01 ON BRSOpBal (MasterCode1,Type,SrNo);
CREATE INDEX BRSOPBAL_02 ON BRSOpBal (MasterCode2);









-- CheckList definition

-- Drop table

-- DROP TABLE CheckList;

CREATE TABLE CheckList (
	Type smallint DEFAULT 0,
	Code integer DEFAULT 0,
	Action smallint DEFAULT 0,
	ActionTime timestamp ,
	UserName text,
	D1 float DEFAULT 0,
	D2 float DEFAULT 0,
	D3 float DEFAULT 0,
	D4 float DEFAULT 0,
	D5 float DEFAULT 0,
	Notes text,
	ComputerName text
);
CREATE INDEX CHECKLIST_21 ON CheckList (Code);
CREATE INDEX CHECKLIST_23 ON CheckList (UserName);
CREATE INDEX CHECKLIST_24 ON CheckList (Action);






-- Config definition

-- Drop table

-- DROP TABLE Config;

CREATE TABLE Config (
	RecType smallint DEFAULT 0,
	Type smallint DEFAULT 0,
	C1 text,
	C2 text,
	C3 text,
	C4 text,
	C5 text,
	C6 text,
	C7 text,
	C8 text,
	C9 text,
	C10 text,
	C11 text,
	C12 text,
	C13 text,
	C14 text,
	C15 text,
	C16 text,
	C17 text,
	C18 text,
	C19 text,
	C20 text,
	C21 text,
	C22 text,
	C23 text,
	C24 text,
	C25 text,
	C26 text,
	C27 text,
	C28 text,
	C29 text,
	C30 text,
	DocName text,
	InvVchName text,
	FaVchName text,
	I1 smallint DEFAULT 0,
	I2 smallint DEFAULT 0,
	I3 smallint DEFAULT 0,
	I4 smallint DEFAULT 0,
	I5 smallint DEFAULT 0,
	I6 smallint DEFAULT 0,
	I7 smallint DEFAULT 0,
	I8 smallint DEFAULT 0,
	I9 smallint DEFAULT 0,
	I10 smallint DEFAULT 0,
	I11 smallint DEFAULT 0,
	I12 smallint DEFAULT 0,
	I13 smallint DEFAULT 0,
	I14 smallint DEFAULT 0,
	I15 smallint DEFAULT 0,
	I16 smallint DEFAULT 0,
	I17 smallint DEFAULT 0,
	I18 smallint DEFAULT 0,
	I19 smallint DEFAULT 0,
	I20 smallint DEFAULT 0,
	I21 smallint DEFAULT 0,
	I22 smallint DEFAULT 0,
	I23 smallint DEFAULT 0,
	I24 smallint DEFAULT 0,
	I25 smallint DEFAULT 0,
	I26 smallint DEFAULT 0,
	I27 smallint DEFAULT 0,
	I28 smallint DEFAULT 0,
	I29 smallint DEFAULT 0,
	I30 smallint DEFAULT 0,
	I31 smallint DEFAULT 0,
	I32 smallint DEFAULT 0,
	I33 smallint DEFAULT 0,
	I34 smallint DEFAULT 0,
	I35 smallint DEFAULT 0,
	NoOfFld smallint DEFAULT 0,
	B1 boolean DEFAULT false,
	B2 boolean DEFAULT false,
	B3 boolean DEFAULT false,
	B4 boolean DEFAULT false,
	B5 boolean DEFAULT false,
	B6 boolean DEFAULT false,
	B7 boolean DEFAULT false,
	B8 boolean DEFAULT false,
	B9 boolean DEFAULT false,
	B10 boolean DEFAULT false,
	B11 boolean DEFAULT false,
	B12 boolean DEFAULT false,
	B13 boolean DEFAULT false,
	B14 boolean DEFAULT false,
	B15 boolean DEFAULT false,
	B16 boolean DEFAULT false,
	B17 boolean DEFAULT false,
	B18 boolean DEFAULT false,
	B19 boolean DEFAULT false,
	B20 boolean DEFAULT false,
	B21 boolean DEFAULT false,
	B22 boolean DEFAULT false,
	B23 boolean DEFAULT false,
	B24 boolean DEFAULT false,
	B25 boolean DEFAULT false,
	B26 boolean DEFAULT false,
	B27 boolean DEFAULT false,
	B28 boolean DEFAULT false,
	B29 boolean DEFAULT false,
	B30 boolean DEFAULT false,
	B31 boolean DEFAULT false,
	B32 boolean DEFAULT false,
	B33 boolean DEFAULT false,
	B34 boolean DEFAULT false,
	B35 boolean DEFAULT false,
	B36 boolean DEFAULT false,
	B37 boolean DEFAULT false,
	B38 boolean DEFAULT false,
	B39 boolean DEFAULT false,
	B40 boolean DEFAULT false,
	B41 boolean DEFAULT false,
	B42 boolean DEFAULT false,
	B43 boolean DEFAULT false,
	B44 boolean DEFAULT false,
	B45 boolean DEFAULT false,
	B46 boolean DEFAULT false,
	B47 boolean DEFAULT false,
	B48 boolean DEFAULT false,
	B49 boolean DEFAULT false,
	B50 boolean DEFAULT false,
	B51 boolean DEFAULT false,
	B52 boolean DEFAULT false,
	B53 boolean DEFAULT false,
	B54 boolean DEFAULT false,
	B55 boolean DEFAULT false,
	B56 boolean DEFAULT false,
	B57 boolean DEFAULT false,
	B58 boolean DEFAULT false,
	B59 boolean DEFAULT false,
	B60 boolean DEFAULT false,
	B61 boolean DEFAULT false,
	B62 boolean DEFAULT false,
	B63 boolean DEFAULT false,
	B64 boolean DEFAULT false,
	B65 boolean DEFAULT false,
	B66 boolean DEFAULT false,
	B67 boolean DEFAULT false,
	B68 boolean DEFAULT false,
	B69 boolean DEFAULT false,
	B70 boolean DEFAULT false,
	B71 boolean DEFAULT false,
	B72 boolean DEFAULT false,
	B73 boolean DEFAULT false,
	B74 boolean DEFAULT false,
	B75 boolean DEFAULT false,
	B76 boolean DEFAULT false,
	B77 boolean DEFAULT false,
	B78 boolean DEFAULT false,
	B79 boolean DEFAULT false,
	B80 boolean DEFAULT false,
	B81 boolean DEFAULT false,
	B82 boolean DEFAULT false,
	B83 boolean DEFAULT false,
	B84 boolean DEFAULT false,
	B85 boolean DEFAULT false,
	B86 boolean DEFAULT false,
	B87 boolean DEFAULT false,
	B88 boolean DEFAULT false,
	B89 boolean DEFAULT false,
	B90 boolean DEFAULT false,
	B91 boolean DEFAULT false,
	B92 boolean DEFAULT false,
	B93 boolean DEFAULT false,
	B94 boolean DEFAULT false,
	B95 boolean DEFAULT false,
	B96 boolean DEFAULT false,
	B97 boolean DEFAULT false,
	B98 boolean DEFAULT false,
	B99 boolean DEFAULT false,
	B100 boolean DEFAULT false,
	B101 boolean DEFAULT false,
	B102 boolean DEFAULT false,
	B103 boolean DEFAULT false,
	B104 boolean DEFAULT false,
	B105 boolean DEFAULT false,
	B106 boolean DEFAULT false,
	B107 boolean DEFAULT false,
	B108 boolean DEFAULT false,
	B109 boolean DEFAULT false,
	B110 boolean DEFAULT false,
	B111 boolean DEFAULT false,
	B112 boolean DEFAULT false,
	B113 boolean DEFAULT false,
	B114 boolean DEFAULT false,
	B115 boolean DEFAULT false,
	B116 boolean DEFAULT false,
	B117 boolean DEFAULT false,
	B118 boolean DEFAULT false,
	B119 boolean DEFAULT false,
	B120 boolean DEFAULT false,
	B121 boolean DEFAULT false,
	B122 boolean DEFAULT false,
	B123 boolean DEFAULT false,
	B124 boolean DEFAULT false,
	B125 boolean DEFAULT false,
	B126 boolean DEFAULT false,
	B127 boolean DEFAULT false,
	B128 boolean DEFAULT false,
	B129 boolean DEFAULT false,
	B130 boolean DEFAULT false,
	B131 boolean DEFAULT false,
	B132 boolean DEFAULT false,
	B133 boolean DEFAULT false,
	B134 boolean DEFAULT false,
	B135 boolean DEFAULT false,
	B136 boolean DEFAULT false,
	B137 boolean DEFAULT false,
	B138 boolean DEFAULT false,
	B139 boolean DEFAULT false,
	B140 boolean DEFAULT false,
	B141 boolean DEFAULT false,
	B142 boolean DEFAULT false,
	L1 integer DEFAULT 0,
	L2 integer DEFAULT 0,
	L3 integer DEFAULT 0,
	L4 integer DEFAULT 0,
	L5 integer DEFAULT 0,
	L6 integer DEFAULT 0,
	L7 integer DEFAULT 0,
	L8 integer DEFAULT 0,
	L9 integer DEFAULT 0,
	L10 integer DEFAULT 0,
	L11 integer DEFAULT 0,
	L12 integer DEFAULT 0,
	L13 integer DEFAULT 0,
	L14 integer DEFAULT 0,
	L15 integer DEFAULT 0,
	L16 integer DEFAULT 0,
	L17 integer DEFAULT 0,
	L18 integer DEFAULT 0,
	L19 integer DEFAULT 0,
	L20 integer DEFAULT 0,
	CM1 integer DEFAULT 0,
	D1 float DEFAULT 0,
	D2 float DEFAULT 0,
	D3 float DEFAULT 0,
	D4 float DEFAULT 0,
	D5 float DEFAULT 0,
	D6 float DEFAULT 0,
	D7 float DEFAULT 0,
	D8 float DEFAULT 0,
	D9 float DEFAULT 0,
	D10 float DEFAULT 0,
	D11 float DEFAULT 0,
	D12 float DEFAULT 0,
	D13 float DEFAULT 0,
	D14 float DEFAULT 0,
	D15 float DEFAULT 0,
	Date timestamp ,
	M1 text,
	PricingMode smallint DEFAULT 0,
	PricingModeForPurc smallint DEFAULT 0,
	M2 text,
	Stamp integer DEFAULT 0
);
CREATE INDEX CONFIG_01 ON Config (RecType,Type);
CREATE INDEX CONFIG_02 ON Config (RecType,L1);
CREATE INDEX CONFIG_03 ON Config (CM1);
CREATE INDEX CONFIG_04 ON Config (C1);






-- DailyMessage definition

-- Drop table

-- DROP TABLE DailyMessage;

CREATE TABLE DailyMessage (
	Date timestamp ,
	NoOfDays smallint DEFAULT 0,
	VchType smallint DEFAULT 0,
	VSCode integer DEFAULT 0,
	Msg1 text,
	Msg2 text,
	Msg3 text,
	Msg4 text
);
CREATE INDEX DAILYMESSAGE_01 ON DailyMessage (Date,VchType,VSCode);






-- DailySum definition

-- Drop table

-- DROP TABLE DailySum;

CREATE TABLE DailySum (
	MasterCode1 integer DEFAULT 0,
	MasterCode2 integer DEFAULT 0,
	MasterType smallint DEFAULT 0,
	Date timestamp ,
	Dr1 float DEFAULT 0,
	Dr2 float DEFAULT 0,
	Dr3 float DEFAULT 0,
	Cr1 float DEFAULT 0,
	Cr2 float DEFAULT 0,
	Cr3 float DEFAULT 0,
	D1 float DEFAULT 0,
	D2 float DEFAULT 0,
	D3 float DEFAULT 0,
	D4 float DEFAULT 0
);
CREATE INDEX DAILYSUM_11 ON DailySum (MasterCode1);
CREATE INDEX DAILYSUM_12 ON DailySum (MasterCode2);
CREATE INDEX DAILYSUM_13 ON DailySum (Date);







-- DataSync definition

-- Drop table

-- DROP TABLE DataSync;

CREATE TABLE DataSync (
	UID integer DEFAULT 0,
	BranchCode integer DEFAULT 0,
	RecType smallint DEFAULT 0,
	Type smallint DEFAULT 0,
	VMType smallint DEFAULT 0,
	MasterName text,
	VchNo text,
	Date timestamp ,
	VchSrCode integer DEFAULT 0,
	CreatedBy text,
	CreationTime timestamp ,
	LastModifiedBy text,
	LastModificationTime timestamp ,
	ApprovedBy text,
	ApprovalTime timestamp ,
	ServerInTime timestamp ,
	M1 text,
	M2 text,
	MasterName1 text,
	ComputerName text,
	OldVchSrName text,
	OldVchType smallint DEFAULT 0,
	VchSrName text,
	DeletedBy text,
	DeletionTime timestamp ,
	Srno smallint DEFAULT 0,
	CheckType smallint DEFAULT 0,
	ClearFullVch boolean DEFAULT false,
	D1 float DEFAULT 0,
	D2 float DEFAULT 0,
	D3 float DEFAULT 0,
	D4 float DEFAULT 0,
	D5 float DEFAULT 0,
	OldMasterName text,
	OldDate timestamp ,
	OldVchNo text,
	OldIdentity text
);
CREATE INDEX DATASYNC_01 ON DataSync (BranchCode,RecType,ServerInTime);







-- DeletedInfo definition

-- Drop table

-- DROP TABLE DeletedInfo;

CREATE TABLE DeletedInfo (
	Type smallint DEFAULT 0,
	VchMastType smallint DEFAULT 0,
	Identity text,
	DeletedBy text,
	DeletionTime timestamp ,
	OrgVchAmtBaseCur float DEFAULT 0,
	ModVchAmtBaseCur float DEFAULT 0,
	ComputerName text
);
CREATE INDEX DELETEDINFO_01 ON DeletedInfo (Type,VchMastType,DeletionTime);








-- EmpLADet definition

-- Drop table

-- DROP TABLE EmpLADet;

CREATE TABLE EmpLADet (
	EmpCode integer DEFAULT 0,
	LAType smallint DEFAULT 0,
	SrNo smallint DEFAULT 0,
	DueDate timestamp ,
	Amount float DEFAULT 0,
	IntAmt float DEFAULT 0,
	Total float DEFAULT 0,
	Remarks text
);
CREATE INDEX EMPLADET_01 ON EmpLADet (EmpCode);
CREATE INDEX EMPLADET_02 ON EmpLADet (LAType);
CREATE INDEX EMPLADET_03 ON EmpLADet (SrNo);
CREATE INDEX EMPLADET_04 ON EmpLADet (DueDate);






-- EventLog definition

-- Drop table

-- DROP TABLE EventLog;

CREATE TABLE EventLog (
	UserName text,
	Date timestamp ,
	WorkedOn smallint DEFAULT 0,
	Description text,
	UID integer DEFAULT 0,
	ComputerName text,
	VersionNo text,
	S1 text,
	SessionId integer DEFAULT 0
);
CREATE INDEX EVENTLOG_01 ON EventLog (UserName);
CREATE INDEX EVENTLOG_02 ON EventLog (Date);
CREATE INDEX EVENTLOG_03 ON EventLog (WorkedOn);
CREATE INDEX EVENTLOG_04 ON EventLog (UID);
CREATE INDEX EVENTLOG_05 ON EventLog (SessionId);






-- Excise definition

-- Drop table

-- DROP TABLE Excise;

CREATE TABLE Excise (
	RecType smallint DEFAULT 0,
	VchCode integer DEFAULT 0,
	DocName text,
	VchNo text,
	SrNo smallint DEFAULT 0,
	Date timestamp ,
	Value float DEFAULT 0,
	Balance float DEFAULT 0,
	Value1 float DEFAULT 0,
	Balance1 float DEFAULT 0,
	Value2 float DEFAULT 0,
	Balance2 float DEFAULT 0,
	Value3 float DEFAULT 0,
	Value4 float DEFAULT 0,
	Value5 float DEFAULT 0,
	ValueType smallint DEFAULT 0,
	SupplierType smallint DEFAULT 0,
	ChallanNo text,
	BankCode text,
	DateOfDeposit timestamp ,
	PeriodEnding timestamp ,
	Dummy smallint DEFAULT 0,
	D1 float DEFAULT 0,
	D2 float DEFAULT 0,
	D3 float DEFAULT 0,
	D4 float DEFAULT 0,
	D5 float DEFAULT 0,
	BranchCode integer DEFAULT 0,
	ClearanceType smallint DEFAULT 0,
	NotificationAvailed text,
	NotificationNo text
);
CREATE INDEX EXCISE_01 ON Excise (RecType,VchCode);
CREATE INDEX EXCISE_02 ON Excise (RecType,Date,ValueType,VchNo,VchCode);







-- ExternalData definition

-- Drop table

-- DROP TABLE ExternalData;

CREATE TABLE ExternalData (
	KeyType smallint DEFAULT 0,
	KeyCode integer DEFAULT 0,
	AppName text,
	CanEditKeyData boolean DEFAULT false,
	CanDeleteKeyData boolean DEFAULT false,
	I1 smallint DEFAULT 0,
	L1 integer DEFAULT 0,
	D1 float DEFAULT 0,
	B1 boolean DEFAULT false,
	DT1 timestamp ,
	C1 text,
	Connected boolean DEFAULT false,
	ConnectedCode integer DEFAULT 0
);
CREATE INDEX EXTERNALDATA_01 ON ExternalData (KeyType,KeyCode);






-- Folio1 definition

-- Drop table

-- DROP TABLE Folio1;

CREATE TABLE Folio1 (
	MasterCode integer DEFAULT 0 NOT NULL,
	MasterType smallint DEFAULT 0,
	D1 float DEFAULT 0,
	D2 float DEFAULT 0,
	D3 float DEFAULT 0,
	D4 float DEFAULT 0,
	D5 float DEFAULT 0,
	D6 float DEFAULT 0,
	D7 float DEFAULT 0,
	D8 float DEFAULT 0,
	D9 float DEFAULT 0,
	D10 float DEFAULT 0,
	D11 float DEFAULT 0,
	D12 float DEFAULT 0,
	D13 float DEFAULT 0,
	D14 float DEFAULT 0,
	D15 float DEFAULT 0,
	D16 float DEFAULT 0,
	D17 float DEFAULT 0,
	D18 float DEFAULT 0,
	D19 float DEFAULT 0,
	D20 float DEFAULT 0,
	D21 float DEFAULT 0,
	D22 float DEFAULT 0,
	D23 float DEFAULT 0,
	D24 float DEFAULT 0,
	D25 float DEFAULT 0,
	D26 float DEFAULT 0,
	D27 float DEFAULT 0,
	D28 float DEFAULT 0,
	D29 float DEFAULT 0,
	D30 float DEFAULT 0,
	D31 float DEFAULT 0,
	D32 float DEFAULT 0,
	D33 float DEFAULT 0,
	D34 float DEFAULT 0,
	D35 float DEFAULT 0,
	D36 float DEFAULT 0,
	D37 float DEFAULT 0,
	D38 float DEFAULT 0,
	D39 float DEFAULT 0,
	D40 float DEFAULT 0,
	D41 float DEFAULT 0,
	D42 float DEFAULT 0,
	D43 float DEFAULT 0,
	D44 float DEFAULT 0,
	D45 float DEFAULT 0,
	D46 float DEFAULT 0,
	D47 float DEFAULT 0,
	D48 float DEFAULT 0,
	D49 float DEFAULT 0,
	D50 float DEFAULT 0,
	D51 float DEFAULT 0,
	D52 float DEFAULT 0,
	D53 float DEFAULT 0,
	D54 float DEFAULT 0,
	D55 float DEFAULT 0,
	D56 float DEFAULT 0,
	D57 float DEFAULT 0,
	D58 float DEFAULT 0,
	D59 float DEFAULT 0,
	D60 float DEFAULT 0,
	D61 float DEFAULT 0,
	D62 float DEFAULT 0,
	D63 float DEFAULT 0,
	D64 float DEFAULT 0,
	D65 float DEFAULT 0,
	D66 float DEFAULT 0,
	D67 float DEFAULT 0,
	D68 float DEFAULT 0,
	D69 float DEFAULT 0,
	D70 float DEFAULT 0,
	D71 float DEFAULT 0,
	D72 float DEFAULT 0,
	D73 float DEFAULT 0,
	D74 float DEFAULT 0,
	D75 float DEFAULT 0,
	D76 float DEFAULT 0,
	D77 float DEFAULT 0,
	D78 float DEFAULT 0,
	D79 float DEFAULT 0,
	D80 float DEFAULT 0,
	D81 float DEFAULT 0,
	D82 float DEFAULT 0,
	D83 float DEFAULT 0,
	D84 float DEFAULT 0,
	D85 float DEFAULT 0,
	D86 float DEFAULT 0,
	D87 float DEFAULT 0,
	D88 float DEFAULT 0,
	D89 float DEFAULT 0,
	D90 float DEFAULT 0,
	D91 float DEFAULT 0,
	D92 float DEFAULT 0,
	D93 float DEFAULT 0,
	D94 float DEFAULT 0,
	D95 float DEFAULT 0,
	D96 float DEFAULT 0,
	D97 float DEFAULT 0,
	D98 float DEFAULT 0,
	D99 float DEFAULT 0,
	D100 float DEFAULT 0,
	D101 float DEFAULT 0,
	D102 float DEFAULT 0,
	D103 float DEFAULT 0,
	D104 float DEFAULT 0,
	D105 float DEFAULT 0,
	D106 float DEFAULT 0,
	D107 float DEFAULT 0,
	D108 float DEFAULT 0,
	D109 float DEFAULT 0,
	D110 float DEFAULT 0,
	D111 float DEFAULT 0,
	D112 float DEFAULT 0,
	D113 float DEFAULT 0,
	D114 float DEFAULT 0,
	D115 float DEFAULT 0,
	D116 float DEFAULT 0,
	D117 float DEFAULT 0,
	D118 float DEFAULT 0,
	D119 float DEFAULT 0,
	D120 float DEFAULT 0,
	D121 float DEFAULT 0,
	D122 float DEFAULT 0,
	D123 float DEFAULT 0,
	D124 float DEFAULT 0,
	D125 float DEFAULT 0,
	D126 float DEFAULT 0,
	D127 float DEFAULT 0,
	D128 float DEFAULT 0,
	D129 float DEFAULT 0,
	D130 float DEFAULT 0,
	D131 float DEFAULT 0,
	D132 float DEFAULT 0,
	D133 float DEFAULT 0,
	D134 float DEFAULT 0,
	D135 float DEFAULT 0,
	D136 float DEFAULT 0,
	D137 float DEFAULT 0,
	D138 float DEFAULT 0,
	D139 float DEFAULT 0,
	D140 float DEFAULT 0,
	D141 float DEFAULT 0,
	D142 float DEFAULT 0,
	D143 float DEFAULT 0,
	D144 float DEFAULT 0,
	D145 float DEFAULT 0,
	D146 float DEFAULT 0,
	D147 float DEFAULT 0,
	D148 float DEFAULT 0,
	D149 float DEFAULT 0,
	D150 float DEFAULT 0,
	B1 boolean DEFAULT false,
	B2 boolean DEFAULT false,
	B3 boolean DEFAULT false,
	B4 boolean DEFAULT false,
	B5 boolean DEFAULT false,
	B6 boolean DEFAULT false,
	B7 boolean DEFAULT false,
	B8 boolean DEFAULT false,
	B9 boolean DEFAULT false,
	B10 boolean DEFAULT false,
	B11 boolean DEFAULT false,
	B12 boolean DEFAULT false,
	CONSTRAINT SYS_PK_12184 PRIMARY KEY (MasterCode)
);
CREATE UNIQUE INDEX SYS_IDX_SYS_PK_12184_12185 ON Folio1 (MasterCode);






-- Help1 definition

-- Drop table

-- DROP TABLE Help1;

CREATE TABLE Help1 (
	RecType smallint DEFAULT 0,
	NameAlias text,
	Code integer DEFAULT 0,
	MasterType smallint DEFAULT 0,
	NameOrAlias smallint DEFAULT 0,
	AdditionalInfo text,
	ParentGroup integer DEFAULT 0,
	MasterSeries integer DEFAULT 0,
	Status smallint DEFAULT 0,
	DefaultMCCode integer DEFAULT 0,
	AddnInfoBt1 text,
	AddnInfoBt2 text,
	AddnInfoBt3 text,
	AddnInfoBt4 text
);
CREATE INDEX HELP1_11 ON Help1 (MasterSeries);
CREATE INDEX HELP1_16 ON Help1 (RecType);
CREATE INDEX HELP1_21 ON Help1 (Status);
CREATE INDEX HELP1_26 ON Help1 (NameAlias);
CREATE INDEX HELP1_31 ON Help1 (MasterType);
CREATE INDEX HELP1_36 ON Help1 (NameOrAlias);
CREATE INDEX HELP1_41 ON Help1 (Code);
CREATE INDEX HELP1_46 ON Help1 (AdditionalInfo);
CREATE INDEX HELP1_81 ON Help1 (NameOrAlias,Code);
CREATE INDEX HELP1_82 ON Help1 (MasterSeries,RecType,Status,NameAlias);






-- Help1AddnInfo definition

-- Drop table

-- DROP TABLE Help1AddnInfo;

CREATE TABLE Help1AddnInfo (
	Code integer DEFAULT 0,
	AddnInfoBt1 text,
	AddnInfoBt2 text,
	AddnInfoBt3 text,
	AddnInfoBt4 text
);
CREATE INDEX HELP1ADDNINFO_21 ON Help1AddnInfo (Code);





-- Help2 definition

-- Drop table

-- DROP TABLE Help2;

CREATE TABLE Help2 (
	RecType1 smallint DEFAULT 0,
	RecType2 smallint DEFAULT 0,
	RecType3 integer DEFAULT 0,
	Name text
);
CREATE INDEX HELP2_01 ON Help2 (RecType1,RecType2,RecType3,Name);






-- ItemDesc definition

-- Drop table

-- DROP TABLE ItemDesc;

CREATE TABLE ItemDesc (
	VchCode integer DEFAULT 0,
	SrNo smallint DEFAULT 0,
	Desc1 text,
	Desc2 text,
	Desc3 text,
	Desc4 text,
	Desc5 text,
	Desc6 text,
	Desc7 text,
	Desc8 text,
	Desc9 text,
	Desc10 text,
	D1 float DEFAULT 0,
	D2 float DEFAULT 0,
	D3 float DEFAULT 0,
	I1 smallint DEFAULT 0
);
CREATE INDEX ITEMDESC_01 ON ItemDesc (VchCode,SrNo);





-- ItemParamDet definition

-- Drop table

-- DROP TABLE ItemParamDet;

CREATE TABLE ItemParamDet (
	Date timestamp ,
	VchType smallint DEFAULT 0,
	VchCode integer DEFAULT 0,
	VchNo text,
	RecType smallint DEFAULT 0,
	VchItemSN smallint DEFAULT 0,
	ItemCode integer DEFAULT 0,
	MCCode integer DEFAULT 0,
	SrNo smallint DEFAULT 0,
	C1 text,
	C2 text,
	C3 text,
	C4 text,
	C5 text,
	C6 text,
	C7 text,
	C8 text,
	C9 text,
	C10 text,
	Value1 float DEFAULT 0,
	Value2 float DEFAULT 0,
	D1 float DEFAULT 0,
	D2 float DEFAULT 0,
	D3 float DEFAULT 0,
	D4 float DEFAULT 0,
	D5 float DEFAULT 0,
	D6 float DEFAULT 0,
	D7 float DEFAULT 0,
	D8 float DEFAULT 0,
	D9 float DEFAULT 0,
	D10 float DEFAULT 0,
	BCN text,
	AutoBCN integer DEFAULT 0,
	OrgDate timestamp 
);
CREATE INDEX ITEMPARAMDET_01 ON ItemParamDet (VchCode,VchItemSN,SrNo);
CREATE INDEX ITEMPARAMDET_02 ON ItemParamDet (ItemCode,MCCode,VchCode,RecType,VchItemSN,SrNo);
CREATE INDEX ITEMPARAMDET_03 ON ItemParamDet (RecType,ItemCode,MCCode,Date,C1,C2,C3,Value1,D3);
CREATE INDEX ITEMPARAMDET_04 ON ItemParamDet (BCN);
CREATE INDEX ITEMPARAMDET_06 ON ItemParamDet (BCN,VchCode);
CREATE INDEX ITEMPARAMDET_07 ON ItemParamDet (BCN,Value1,MCCode);






-- ItemSerialNo definition

-- Drop table

-- DROP TABLE ItemSerialNo;

CREATE TABLE ItemSerialNo (
	VchCode integer DEFAULT 0,
	VchType smallint DEFAULT 0,
	VchNo text,
	VchItemSN smallint DEFAULT 0,
	Date timestamp ,
	ItemCode integer DEFAULT 0,
	MCCode integer DEFAULT 0,
	GridSN integer DEFAULT 0,
	SerialNo text,
	AutoSrNo integer DEFAULT 0,
	Value1 float DEFAULT 0,
	Value2 float DEFAULT 0,
	D1 float DEFAULT 0,
	D2 float DEFAULT 0,
	D3 float DEFAULT 0,
	D4 float DEFAULT 0,
	MonthVal smallint DEFAULT 0,
	C1 text,
	C2 text,
	C3 text,
	C4 text,
	C5 text,
	C6 text,
	C7 text,
	C8 text,
	C9 text,
	C10 text,
	WarrantyMonth smallint DEFAULT 0
);
CREATE INDEX ITEMSERIALNO_01 ON ItemSerialNo (ItemCode,SerialNo,Date,VchType,VchNo,VchCode);
CREATE INDEX ITEMSERIALNO_02 ON ItemSerialNo (VchCode,VchItemSN,GridSN);
CREATE INDEX ITEMSERIALNO_03 ON ItemSerialNo (ItemCode,MCCode,SerialNo,Value1,Date,VchCode);
CREATE INDEX ITEMSERIALNO_04 ON ItemSerialNo (ItemCode,SerialNo,Value1,Date,VchCode);
CREATE INDEX ITEMSERIALNO_05 ON ItemSerialNo (ItemCode,MCCode,VchCode,VchItemSN,GridSN,SerialNo);
CREATE INDEX ITEMSERIALNO_06 ON ItemSerialNo (ItemCode,Value1,Date,VchType,VchCode,VchItemSN,GridSN,SerialNo);
CREATE INDEX ITEMSERIALNO_07 ON ItemSerialNo (ItemCode,VchType,VchCode,AutoSrNo);
CREATE INDEX ITEMSERIALNO_08 ON ItemSerialNo (ItemCode,MCCode,VchCode,SerialNo,Value1);
CREATE INDEX ITEMSERIALNO_09 ON ItemSerialNo (ItemCode,MCCode,SerialNo,Value1);
CREATE INDEX ITEMSERIALNO_10 ON ItemSerialNo (ItemCode,AutoSrNo);
CREATE INDEX ITEMSERIALNO_11 ON ItemSerialNo (ItemCode,Date,AutoSrNo);
CREATE INDEX ITEMSERIALNO_12 ON ItemSerialNo (ItemCode,MonthVal,AutoSrNo);
CREATE INDEX ITEMSERIALNO_13 ON ItemSerialNo (SerialNo,Value1,MCCode);







-- ItemSNInstallDet definition

-- Drop table

-- DROP TABLE ItemSNInstallDet;

CREATE TABLE ItemSNInstallDet (
	InstallCode integer DEFAULT 0,
	InstallDate timestamp ,
	ItemCode integer DEFAULT 0,
	SerialNo text,
	InvoiceNo text,
	InvoiceDate timestamp ,
	PartyCode integer DEFAULT 0,
	Organization text,
	TradeDesc text,
	ContactPerson text,
	Designation text,
	Address1 text,
	Address2 text,
	CountryCode integer DEFAULT 0,
	StateCode integer DEFAULT 0,
	CityCode integer DEFAULT 0,
	PinCode text,
	MobileNo text,
	PhoneNo text,
	FaxNo text,
	EmailID text,
	Narration text,
	WarrMonth smallint DEFAULT 0
);
CREATE INDEX ITEMSNINSTALLDET_01 ON ItemSNInstallDet (ItemCode,SerialNo);
CREATE INDEX ITEMSNINSTALLDET_02 ON ItemSNInstallDet (InstallCode);
CREATE INDEX ITEMSNINSTALLDET_03 ON ItemSNInstallDet (PartyCode);
CREATE INDEX ITEMSNINSTALLDET_04 ON ItemSNInstallDet (CountryCode);
CREATE INDEX ITEMSNINSTALLDET_05 ON ItemSNInstallDet (StateCode);
CREATE INDEX ITEMSNINSTALLDET_06 ON ItemSNInstallDet (CityCode);





-- JobFinishedRefs definition

-- Drop table

-- DROP TABLE JobFinishedRefs;

CREATE TABLE JobFinishedRefs (
	JobID text,
	TranType smallint DEFAULT 0,
	VchCode integer DEFAULT 0,
	MasterCode1 integer DEFAULT 0,
	MasterCode2 integer DEFAULT 0,
	SrNo smallint DEFAULT 0,
	VchType smallint DEFAULT 0,
	Date timestamp ,
	VchNo text,
	VchSeriesCode integer DEFAULT 0,
	CM1 integer DEFAULT 0,
	Value1 float DEFAULT 0,
	Value2 float DEFAULT 0,
	C1 text,
	C2 text,
	C3 text,
	Date1 timestamp ,
	Rectype smallint DEFAULT 0
);
CREATE INDEX JOBFINISHEDREFS_01 ON JobFinishedRefs (MasterCode1);
CREATE INDEX JOBFINISHEDREFS_02 ON JobFinishedRefs (JobID);
CREATE INDEX JOBFINISHEDREFS_03 ON JobFinishedRefs (Date);
CREATE INDEX JOBFINISHEDREFS_04 ON JobFinishedRefs (CM1);
CREATE INDEX JOBFINISHEDREFS_05 ON JobFinishedRefs (TranType);
CREATE INDEX JOBFINISHEDREFS_06 ON JobFinishedRefs (VchType);
CREATE INDEX JOBFINISHEDREFS_07 ON JobFinishedRefs (MasterCode2);







-- Locks definition

-- Drop table

-- DROP TABLE Locks;

CREATE TABLE Locks (
	Type timestamp ,
	IBR boolean DEFAULT false,
	MBU boolean DEFAULT false,
	CSU boolean DEFAULT false,
	STU boolean DEFAULT false,
	Working boolean DEFAULT false,
	BSSTD boolean DEFAULT false,
	TERBR boolean DEFAULT false,
	BRS boolean DEFAULT false,
	CCCF boolean DEFAULT false,
	SuppTypeF boolean DEFAULT false,
	BSNF boolean DEFAULT false,
	BST boolean DEFAULT false,
	OSPO boolean DEFAULT false,
	OBAMC boolean DEFAULT false,
	TDSSHE boolean DEFAULT false,
	TESRNO boolean DEFAULT false,
	MAJOR smallint DEFAULT 0,
	MINOR smallint DEFAULT 0,
	RW35 boolean DEFAULT false,
	MEBR boolean DEFAULT false,
	MEBR1 boolean DEFAULT false,
	MFFSA boolean DEFAULT false,
	SMPL boolean DEFAULT false,
	GSTU boolean DEFAULT false,
	MUSPO boolean DEFAULT false,
	DFYW boolean DEFAULT false,
	BATCH boolean DEFAULT false,
	BATCHMRPSRNOPARAM boolean DEFAULT false,
	ENTRYTAXRATE boolean DEFAULT false,
	STPTMC boolean DEFAULT false,
	CHALLANNO boolean DEFAULT false,
	PARAMDET boolean DEFAULT false,
	MASTFP boolean DEFAULT false,
	MASTFP1 boolean DEFAULT false,
	RMVLOCDB boolean DEFAULT false,
	POSSERIESFTBSNAME boolean DEFAULT false,
	STSCGUPDT boolean DEFAULT false,
	ItemSrNoLen boolean DEFAULT false,
	RGMAST boolean DEFAULT false,
	MainDbVer smallint DEFAULT 0,
	PartialDbVer smallint DEFAULT 0,
	COMPEGRPMAST boolean DEFAULT false,
	COMPCONTGRPMAST boolean DEFAULT false,
	AREAMAST boolean DEFAULT false,
	CONTDEPTMAST boolean DEFAULT false,
	SOURCEMAST boolean DEFAULT false,
	SUBSTATUSMAST boolean DEFAULT false,
	NXTACTIONMAST boolean DEFAULT false,
	TRADEMAST boolean DEFAULT false,
	B1 boolean DEFAULT false,
	FAQGRPMAST boolean DEFAULT false,
	PENDSUBSTATUSMAST boolean DEFAULT false,
	TRACKINGNO boolean DEFAULT false,
	WinUser text,
	TOFQ boolean DEFAULT false,
	URefBal boolean DEFAULT false
);






-- Master1 definition

-- Drop table

-- DROP TABLE Master1;

CREATE TABLE Master1 (
    companyid integer DEFAULT 0,
	Code integer DEFAULT 0 NOT NULL,
	MasterType smallint DEFAULT 0,
	Name text,
	Alias text,
	PrintName text,
	ParentGrp integer DEFAULT 0,
	Stamp integer DEFAULT 0,
	CM1 integer DEFAULT 0,
	CM2 integer DEFAULT 0,
	CM3 integer DEFAULT 0,
	CM4 integer DEFAULT 0,
	CM5 integer DEFAULT 0,
	CM6 integer DEFAULT 0,
	CM7 integer DEFAULT 0,
	CM8 integer DEFAULT 0,
	CM9 integer DEFAULT 0,
	CM10 integer DEFAULT 0,
	CM11 integer DEFAULT 0,
	D1 float DEFAULT 0,
	D2 float DEFAULT 0,
	D3 float DEFAULT 0,
	D4 float DEFAULT 0,
	D5 float DEFAULT 0,
	D6 float DEFAULT 0,
	D7 float DEFAULT 0,
	D8 float DEFAULT 0,
	D9 float DEFAULT 0,
	D10 float DEFAULT 0,
	D11 float DEFAULT 0,
	D12 float DEFAULT 0,
	D13 float DEFAULT 0,
	D14 float DEFAULT 0,
	D15 float DEFAULT 0,
	D16 float DEFAULT 0,
	D17 float DEFAULT 0,
	D18 float DEFAULT 0,
	D19 float DEFAULT 0,
	D20 float DEFAULT 0,
	D21 float DEFAULT 0,
	D22 float DEFAULT 0,
	D23 float DEFAULT 0,
	D24 float DEFAULT 0,
	D25 float DEFAULT 0,
	I1 smallint DEFAULT 0,
	I2 smallint DEFAULT 0,
	I3 smallint DEFAULT 0,
	I4 smallint DEFAULT 0,
	I5 smallint DEFAULT 0,
	I6 smallint DEFAULT 0,
	I7 smallint DEFAULT 0,
	I8 smallint DEFAULT 0,
	I9 smallint DEFAULT 0,
	I10 smallint DEFAULT 0,
	I11 smallint DEFAULT 0,
	I12 smallint DEFAULT 0,
	I13 smallint DEFAULT 0,
	I14 smallint DEFAULT 0,
	I15 smallint DEFAULT 0,
	I16 smallint DEFAULT 0,
	I17 smallint DEFAULT 0,
	I18 smallint DEFAULT 0,
	I19 smallint DEFAULT 0,
	I20 smallint DEFAULT 0,
	I21 smallint DEFAULT 0,
	I22 smallint DEFAULT 0,
	I23 smallint DEFAULT 0,
	I24 smallint DEFAULT 0,
	Level smallint DEFAULT 0,
	SrNo smallint DEFAULT 0,
	B1 boolean DEFAULT false,
	B2 boolean DEFAULT false,
	B3 boolean DEFAULT false,
	B4 boolean DEFAULT false,
	B5 boolean DEFAULT false,
	B6 boolean DEFAULT false,
	B7 boolean DEFAULT false,
	B8 boolean DEFAULT false,
	B9 boolean DEFAULT false,
	B10 boolean DEFAULT false,
	B11 boolean DEFAULT false,
	B12 boolean DEFAULT false,
	B13 boolean DEFAULT false,
	B14 boolean DEFAULT false,
	B15 boolean DEFAULT false,
	B16 boolean DEFAULT false,
	B17 boolean DEFAULT false,
	B18 boolean DEFAULT false,
	B19 boolean DEFAULT false,
	B20 boolean DEFAULT false,
	B21 boolean DEFAULT false,
	B22 boolean DEFAULT false,
	B23 boolean DEFAULT false,
	B24 boolean DEFAULT false,
	B25 boolean DEFAULT false,
	B26 boolean DEFAULT false,
	B27 boolean DEFAULT false,
	B28 boolean DEFAULT false,
	B29 boolean DEFAULT false,
	B30 boolean DEFAULT false,
	B31 boolean DEFAULT false,
	B32 boolean DEFAULT false,
	B33 boolean DEFAULT false,
	B34 boolean DEFAULT false,
	B35 boolean DEFAULT false,
	B36 boolean DEFAULT false,
	External boolean DEFAULT false,
	C1 text,
	C2 text,
	L1 integer DEFAULT 0,
	L2 integer DEFAULT 0,
	Notes1 text,
	Notes2 text,
	MasterNotes text,
	CreatedBy text,
	CreationTime timestamp ,
	ModifiedBy text,
	ModificationTime timestamp ,
	AuthorisedBy text,
	AuthorisationTime timestamp ,
	ApprovalStatus smallint DEFAULT 0,
	SyncStatus boolean DEFAULT false,
	MasterSeriesGrp text,
	Source smallint DEFAULT 0,
	BlockedMaster boolean DEFAULT false,
	BlockedNotes text,
	DeactiveMaster boolean DEFAULT false,
	C3 text,
	C4 text,
	BlockedVchType text,
	C5 text,
	C6 text,
	M1 text,
	TPF1 boolean DEFAULT false,
	TPF2 boolean DEFAULT false,
	RejectionStatus smallint DEFAULT 0,
	OldIdentity text,
	PRIMARY KEY(companyid, Code)
);
CREATE INDEX MASTER1_02 ON Master1 (MasterType,Name);
CREATE INDEX MASTER1_03 ON Master1 (MasterType,Alias);
CREATE INDEX MASTER1_04 ON Master1 (CM1);
CREATE INDEX MASTER1_05 ON Master1 (CM2);
CREATE INDEX MASTER1_06 ON Master1 (CM3);
CREATE INDEX MASTER1_07 ON Master1 (CM4);
CREATE INDEX MASTER1_08 ON Master1 (CM5);
CREATE INDEX MASTER1_17 ON Master1 (CM6);
CREATE INDEX MASTER1_18 ON Master1 (CM7);
CREATE INDEX MASTER1_20 ON Master1 (CM8);
CREATE INDEX MASTER1_31 ON Master1 (MasterType);
CREATE INDEX MASTER1_32 ON Master1 (Name);
CREATE INDEX MASTER1_33 ON Master1 (Alias);
CREATE INDEX MASTER1_34 ON Master1 (ParentGrp);
CREATE INDEX MASTER1_35 ON Master1 (D11);
CREATE INDEX MASTER1_36 ON Master1 (C2);
CREATE INDEX MASTER1_37 ON Master1 (SyncStatus);
CREATE INDEX MASTER1_38 ON Master1 (Source);
CREATE INDEX MASTER1_39 ON Master1 (I10);
CREATE INDEX MASTER1_40 ON Master1 (CM9);
CREATE INDEX MASTER1_41 ON Master1 (CM10);
CREATE INDEX MASTER1_42 ON Master1 (CM11);
CREATE INDEX MASTER1_81 ON Master1 (Code);
CREATE UNIQUE INDEX SYS_IDX_SYS_PK_12189_12190 ON Master1 (Code,companyid);






-- MasterAddressInfo definition

-- Drop table

-- DROP TABLE MasterAddressInfo;

CREATE TABLE MasterAddressInfo (
	MasterCode integer DEFAULT 0 NOT NULL,
	Address1 text,
	Address2 text,
	Address3 text,
	Address4 text,
	TelNo text,
	Fax text,
	Email text,
	Mobile text,
	LST text,
	CST text,
	ST37 text,
	TINNo text,
	LBTNo text,
	ITPAN text,
	ITWard text,
	Contact text,
	ExciseRegNo text,
	ECCCode text,
	PLANo text,
	Division text,
	Range text,
	Collectorate text,
	OF1 text,
	OF2 text,
	OF3 text,
	OF4 text,
	OF5 text,
	OF6 text,
	OF7 text,
	OF8 text,
	OF9 text,
	OF10 text,
	SupplierType text,
	ServiceTaxNo text,
	TelNoResi text,
	GSTNo text,
	CountryCodeLong integer DEFAULT 0,
	StateCodeLong integer DEFAULT 0,
	CityCodeLong integer DEFAULT 0,
	RegionCodeLong integer DEFAULT 0,
	AreaCodeLong integer DEFAULT 0,
	ContDeptCodeLong integer DEFAULT 0,
	PINCode text,
	DLNo text,
	DLNo2 text,
	Transport text,
	Station text,
	AccNo text,
	Date1 timestamp ,
	Date2 timestamp ,
	Date3 timestamp ,
	Date4 timestamp ,
	Date5 timestamp ,
	Date6 timestamp ,
	Date7 timestamp ,
	Date8 timestamp ,
	C1 text,
	C2 text,
	C3 text,
	C4 text,
	C5 text,
	C6 text,
	C7 text,
	C8 text,
	C9 text,
	C10 text,
	M1 text,
	CONSTRAINT SYS_PK_12194 PRIMARY KEY (MasterCode)
);
CREATE INDEX MASTERADDRESSINFO_02 ON MasterAddressInfo (CountryCodeLong);
CREATE INDEX MASTERADDRESSINFO_03 ON MasterAddressInfo (StateCodeLong);
CREATE INDEX MASTERADDRESSINFO_04 ON MasterAddressInfo (CityCodeLong);
CREATE INDEX MASTERADDRESSINFO_05 ON MasterAddressInfo (RegionCodeLong);
CREATE INDEX MASTERADDRESSINFO_06 ON MasterAddressInfo (Mobile);
CREATE INDEX MASTERADDRESSINFO_07 ON MasterAddressInfo (Email);
CREATE UNIQUE INDEX SYS_IDX_SYS_PK_12194_12195 ON MasterAddressInfo (MasterCode);







-- MasterSupport definition

-- Drop table

-- DROP TABLE MasterSupport;

CREATE TABLE MasterSupport (
	MasterCode integer DEFAULT 0,
	CM1 integer DEFAULT 0,
	CM2 integer DEFAULT 0,
	CM3 integer DEFAULT 0,
	D1 float DEFAULT 0,
	D2 float DEFAULT 0,
	D3 float DEFAULT 0,
	D4 float DEFAULT 0,
	D5 float DEFAULT 0,
	D6 float DEFAULT 0,
	D7 float DEFAULT 0,
	I1 smallint DEFAULT 0,
	I2 smallint DEFAULT 0,
	I3 smallint DEFAULT 0,
	I4 smallint DEFAULT 0,
	I5 smallint DEFAULT 0,
	I6 smallint DEFAULT 0,
	I7 smallint DEFAULT 0,
	I8 smallint DEFAULT 0,
	I9 smallint DEFAULT 0,
	Date timestamp ,
	MasterType smallint DEFAULT 0,
	C1 text,
	B1 boolean DEFAULT false,
	C2 text,
	C3 text,
	C4 text,
	C5 text,
	B2 boolean DEFAULT false,
	B3 boolean DEFAULT false,
	B4 boolean DEFAULT false,
	D8 float DEFAULT 0,
	D9 float DEFAULT 0,
	D10 float DEFAULT 0,
	D11 float DEFAULT 0,
	D12 float DEFAULT 0,
	RecType smallint DEFAULT 0,
	Date1 timestamp ,
	CM4 integer DEFAULT 0,
	CM5 integer DEFAULT 0,
	Date2 timestamp ,
	Date3 timestamp ,
	M1 text
);
CREATE INDEX MASTERSUPPORT_03 ON MasterSupport (CM2);
CREATE INDEX MASTERSUPPORT_04 ON MasterSupport (CM3);
CREATE INDEX MASTERSUPPORT_11 ON MasterSupport (MasterCode);
CREATE INDEX MASTERSUPPORT_12 ON MasterSupport (CM1);
CREATE INDEX MASTERSUPPORT_13 ON MasterSupport (MasterType);
CREATE INDEX MASTERSUPPORT_14 ON MasterSupport (Date);
CREATE INDEX MASTERSUPPORT_15 ON MasterSupport (I1);
CREATE INDEX MASTERSUPPORT_16 ON MasterSupport (I2);
CREATE INDEX MASTERSUPPORT_17 ON MasterSupport (C1);
CREATE INDEX MASTERSUPPORT_18 ON MasterSupport (RecType);
CREATE INDEX MASTERSUPPORT_19 ON MasterSupport (Date1);
CREATE INDEX MASTERSUPPORT_20 ON MasterSupport (CM4);
CREATE INDEX MASTERSUPPORT_21 ON MasterSupport (CM5);






-- MastFootPrint definition

-- Drop table

-- DROP TABLE MastFootPrint;

CREATE TABLE MastFootPrint (
    comapnyid integer DEFAULT 0,
	MasterCode integer DEFAULT 0,
	Name text,
	MasterType smallint DEFAULT 0,
	Stamp integer DEFAULT 0,
	PartialFP text,
	RemainFP text,
	primary key (MasterCode,comapnyid)
);
CREATE INDEX MASTFOOTPRINT_01 ON MastFootPrint (MasterCode);
CREATE INDEX MASTFOOTPRINT_02 ON MastFootPrint (MasterType,Name);





-- OEDDet definition

-- Drop table

-- DROP TABLE OEDDet;

CREATE TABLE OEDDet (
	VchCode integer DEFAULT 0,
	OEDRate float DEFAULT 0,
	OEDAmount float DEFAULT 0,
	CessRate float DEFAULT 0,
	CessAmount float DEFAULT 0,
	HECessRate float DEFAULT 0,
	HECessAmount float DEFAULT 0,
	D1 float DEFAULT 0,
	I1 smallint DEFAULT 0,
	L1 integer DEFAULT 0
);
CREATE INDEX OEDDET_01 ON OEDDet (VchCode);






-- OrgSalePurc definition

-- Drop table

-- DROP TABLE OrgSalePurc;

CREATE TABLE OrgSalePurc (
	VchCode integer DEFAULT 0,
	VchNo text,
	VchDate timestamp ,
	TaxableAmt float DEFAULT 0,
	TaxAmt float DEFAULT 0,
	RegType smallint DEFAULT 0
);
CREATE INDEX ORGSALEPURC_01 ON OrgSalePurc (VchCode);





-- PackingDetails definition

-- Drop table

-- DROP TABLE PackingDetails;

CREATE TABLE PackingDetails (
	SrNo integer DEFAULT 0,
	VchCode integer DEFAULT 0,
	PackageNo text,
	Weight float DEFAULT 0,
	EstimatedValue float DEFAULT 0,
	Size text,
	Description text,
	Remarks text,
	MarkaNo text,
	Quantity float DEFAULT 0,
	Unit integer DEFAULT 0,
	PackingMode text
);
CREATE INDEX PACKINGDETAILS_01 ON PackingDetails (SrNo);
CREATE INDEX PACKINGDETAILS_02 ON PackingDetails (PackageNo);
CREATE INDEX PACKINGDETAILS_03 ON PackingDetails (VchCode);
CREATE INDEX PACKINGDETAILS_04 ON PackingDetails (Unit);





-- Patches definition

-- Drop table

-- DROP TABLE Patches;

CREATE TABLE Patches (
	DummyFld boolean DEFAULT false,
	MasterNotes boolean DEFAULT false,
	MBO boolean DEFAULT false,
	UFSU boolean DEFAULT false,
	DUFITC boolean DEFAULT false,
	CheckList boolean DEFAULT false,
	SPACC boolean DEFAULT false,
	UMBDB1 boolean DEFAULT false,
	BCNAltQty boolean DEFAULT false,
	UMB1 boolean DEFAULT false,
	ExpBatch boolean DEFAULT false,
	QuoteDefaultSeries boolean DEFAULT false,
	BatchStkTfr boolean DEFAULT false,
	ImpactBSSalePurc boolean DEFAULT false,
	DiscMarkupConfig boolean DEFAULT false,
	PickQtnAltQty boolean DEFAULT false,
	VchAudit boolean DEFAULT false,
	DiscHelpData boolean DEFAULT false,
	ItemSrNoLen boolean DEFAULT false,
	SalaryDefaultSeries boolean DEFAULT false,
	FinalResults boolean DEFAULT false,
	PDCT3 boolean DEFAULT false,
	PaidDays boolean DEFAULT false,
	PUSJMC boolean DEFAULT false,
	CRSalesDefaultSeries boolean DEFAULT false,
	UFRD boolean DEFAULT false,
	DefaultSettlementMode boolean DEFAULT false,
	DefaultExciseType boolean DEFAULT false,
	BatchDate smallint DEFAULT 0,
	IndentDefaultSeries boolean DEFAULT false,
	UserRights boolean DEFAULT false,
	AccCodes boolean DEFAULT false,
	ItemMastDefaultPrice boolean DEFAULT false,
	ItemMastTreatMRPAsSP boolean DEFAULT false,
	Help1AddnInfo boolean DEFAULT false,
	ItemParamNettAmt boolean DEFAULT false,
	UpgradeForSchemeMast boolean DEFAULT false,
	TEMCWiseRef boolean DEFAULT false,
	SupplierDutyDet boolean DEFAULT false
);






-- PhyStkSubDet definition

-- Drop table

-- DROP TABLE PhyStkSubDet;

CREATE TABLE PhyStkSubDet (
	RecType smallint DEFAULT 0,
	VchCode integer DEFAULT 0,
	VchType smallint DEFAULT 0,
	VchNo text,
	MasterCode1 integer DEFAULT 0,
	MasterCode2 integer DEFAULT 0,
	SrNo smallint DEFAULT 0,
	Date timestamp ,
	DueDate timestamp ,
	No text,
	Value1 float DEFAULT 0,
	Value2 float DEFAULT 0,
	Value3 float DEFAULT 0,
	Balance1 float DEFAULT 0,
	Balance2 float DEFAULT 0,
	Balance3 float DEFAULT 0,
	ItemSrNo smallint DEFAULT 0,
	MfgDate timestamp ,
	NewRefAmount float DEFAULT 0,
	MonthVal smallint DEFAULT 0,
	WarrantyMonth smallint DEFAULT 0,
	OrgDate timestamp ,
	C1 text,
	C2 text,
	C3 text,
	C4 text,
	C5 text,
	C6 text,
	C7 text,
	C8 text,
	C9 text,
	C10 text,
	D1 float DEFAULT 0,
	D2 float DEFAULT 0,
	D3 float DEFAULT 0,
	D4 float DEFAULT 0,
	D5 float DEFAULT 0,
	D6 float DEFAULT 0,
	B1 boolean DEFAULT false
);
CREATE INDEX PHYSTKSUBDET_01 ON PhyStkSubDet (MasterCode1);
CREATE INDEX PHYSTKSUBDET_02 ON PhyStkSubDet (MasterCode2);
CREATE INDEX PHYSTKSUBDET_03 ON PhyStkSubDet (Date);
CREATE INDEX PHYSTKSUBDET_04 ON PhyStkSubDet (VchType);
CREATE INDEX PHYSTKSUBDET_05 ON PhyStkSubDet (VchCode);
CREATE INDEX PHYSTKSUBDET_06 ON PhyStkSubDet (RecType);
CREATE INDEX PHYSTKSUBDET_07 ON PhyStkSubDet (SrNo);
CREATE INDEX PHYSTKSUBDET_08 ON PhyStkSubDet (No);





-- POSDet definition

-- Drop table

-- DROP TABLE POSDet;

CREATE TABLE POSDet (
	VchCode integer DEFAULT 0,
	CashAmt float DEFAULT 0,
	ChequeAmt float DEFAULT 0,
	CCAmt1 float DEFAULT 0,
	CCAmt2 float DEFAULT 0,
	CCAmt3 float DEFAULT 0,
	CashNarr text,
	ChequeNarr text,
	CCNarr1 text,
	CCNarr2 text,
	CCNarr3 text,
	CashRecdAmt float DEFAULT 0,
	CashAccCode integer DEFAULT 0,
	CCAccCode1 integer DEFAULT 0,
	CCAccCode2 integer DEFAULT 0,
	CCAccCode3 integer DEFAULT 0,
	ChequeAccCode integer DEFAULT 0
);
CREATE INDEX POSDET_01 ON POSDet (VchCode);





-- RepColSize definition

-- Drop table

-- DROP TABLE RepColSize;

CREATE TABLE RepColSize (
	RepID smallint DEFAULT 0,
	SubID smallint DEFAULT 0,
	ColID smallint DEFAULT 0,
	ColSize integer DEFAULT 0,
	FormatName text,
	CustomRepFormatName text,
	WideScreen boolean DEFAULT false
);
CREATE INDEX REPCOLSIZE_01 ON RepColSize (RepID);
CREATE INDEX REPCOLSIZE_02 ON RepColSize (RepID,SubID);




-- RepOptValues definition

-- Drop table

-- DROP TABLE RepOptValues;

CREATE TABLE RepOptValues (
	RepID smallint DEFAULT 0,
	ReportType smallint DEFAULT 0,
	ValueType smallint DEFAULT 0,
	Value text,
	MasterType smallint DEFAULT 0,
	FieldID smallint DEFAULT 0,
	FieldValue text,
	SubRepID smallint DEFAULT 0,
	FormatName text
);
CREATE INDEX REPOPTVALUES_01 ON RepOptValues (RepID,ReportType);





-- STDet definition

-- Drop table

-- DROP TABLE STDet;

CREATE TABLE STDet (
	VchCode integer DEFAULT 0,
	STCategory smallint DEFAULT 0,
	STAssValue float DEFAULT 0,
	STRate float DEFAULT 0,
	SBCRate float DEFAULT 0,
	KKCRate float DEFAULT 0,
	STCessRate float DEFAULT 0,
	STHECessRate float DEFAULT 0
);
CREATE INDEX STDET_01 ON STDet (VchCode);




-- TDS definition

-- Drop table

-- DROP TABLE TDS;

CREATE TABLE TDS (
	Method smallint DEFAULT 0,
	RefNo text,
	RefCode integer DEFAULT 0,
	SrNo smallint DEFAULT 0,
	VchCode integer DEFAULT 0,
	VchType smallint DEFAULT 0,
	MasterCode1 integer DEFAULT 0,
	MasterCode2 integer DEFAULT 0,
	EntryDate timestamp ,
	DateOfCredit timestamp ,
	VchAmt float DEFAULT 0,
	TDSRate float DEFAULT 0,
	TDSAmt float DEFAULT 0,
	SurchargeRate float DEFAULT 0,
	SurchargeAmt float DEFAULT 0,
	CessRate float DEFAULT 0,
	CessAmt float DEFAULT 0,
	SHECessRate float DEFAULT 0,
	SHECessAmt float DEFAULT 0,
	Interest float DEFAULT 0,
	OtherAmt float DEFAULT 0,
	LowerRate boolean DEFAULT false,
	Reason text,
	ChallanNo text,
	ChequeNo text,
	ChequeDate timestamp ,
	Quarter smallint DEFAULT 0,
	RecType smallint DEFAULT 0
);
CREATE INDEX TDS_01 ON TDS (MasterCode2,Method,EntryDate,VchCode);
CREATE INDEX TDS_02 ON TDS (MasterCode1,Method,RefNo);
CREATE INDEX TDS_03 ON TDS (VchCode,MasterCode1,SrNo);
CREATE INDEX TDS_04 ON TDS (RefCode,Method);
CREATE INDEX TDS_05 ON TDS (RecType);





-- TradingExcise definition

-- Drop table

-- DROP TABLE TradingExcise;

CREATE TABLE TradingExcise (
	RefCode integer DEFAULT 0,
	Stamp integer DEFAULT 0,
	Method smallint DEFAULT 0,
	VchCode integer DEFAULT 0,
	SrNo smallint DEFAULT 0,
	VchType smallint DEFAULT 0,
	RefNo text,
	PartyCode integer DEFAULT 0,
	VchNo text,
	Date timestamp ,
	ItemCode integer DEFAULT 0,
	Qty float DEFAULT 0,
	Balance float DEFAULT 0,
	Status smallint DEFAULT 0,
	AssValue float DEFAULT 0,
	DutyRate float DEFAULT 0,
	DutyType smallint DEFAULT 0,
	DutyAmt float DEFAULT 0,
	DutyRate1 float DEFAULT 0,
	DutyType1 smallint DEFAULT 0,
	DutyAmt1 float DEFAULT 0,
	DutyRate2 float DEFAULT 0,
	DutyType2 smallint DEFAULT 0,
	DutyAmt2 float DEFAULT 0,
	DutyRate3 float DEFAULT 0,
	DutyType3 smallint DEFAULT 0,
	DutyAmt3 float DEFAULT 0,
	MfrQty float DEFAULT 0,
	MfrCode integer DEFAULT 0,
	MfrBillNo text,
	MfrBillDate timestamp ,
	RG23DPageNo text,
	RG23DSrNo text,
	AutoRG23DPageNo integer DEFAULT 0,
	AutoRG23DSrNo integer DEFAULT 0,
	SuppRG23DPageNo text,
	SuppRG23DSrNo text,
	MCCode integer DEFAULT 0,
	SuppAssValue float DEFAULT 0,
	SuppDutyAmt float DEFAULT 0,
	SuppDutyAmt1 float DEFAULT 0,
	SuppDutyAmt2 float DEFAULT 0,
	SuppDutyAmt3 float DEFAULT 0,
	CarryRefZeroQty boolean DEFAULT false,
	MfrInvoicePrepDateTime text,
	MfrGoodsRemovalDateTime text,
	ActualSuppAssValue float DEFAULT 0,
	ActualSuppDutyAmt float DEFAULT 0,
	ActualSuppDutyAmt1 float DEFAULT 0,
	ActualSuppDutyAmt2 float DEFAULT 0,
	ActualSuppDutyAmt3 float DEFAULT 0,
	ActualSuppQty float DEFAULT 0,
	SuppOrgDetailsSpecified boolean DEFAULT false
);
CREATE INDEX TRADINGEXCISE_01 ON TradingExcise (RefCode,Method,Date,VchType,VchNo,VchCode);
CREATE INDEX TRADINGEXCISE_02 ON TradingExcise (ItemCode,Method,Status);
CREATE INDEX TRADINGEXCISE_03 ON TradingExcise (ItemCode,Method,RefNo);
CREATE INDEX TRADINGEXCISE_04 ON TradingExcise (VchCode,ItemCode,SrNo);
CREATE INDEX TRADINGEXCISE_05 ON TradingExcise (VchCode,ItemCode,RefNo);
CREATE INDEX TRADINGEXCISE_06 ON TradingExcise (MCCode,ItemCode,Method,Status);
CREATE INDEX TRADINGEXCISE_07 ON TradingExcise (MCCode,ItemCode,Method,RefNo);
CREATE INDEX TRADINGEXCISE_08 ON TradingExcise (VchCode,MCCode,ItemCode,SrNo);
CREATE INDEX TRADINGEXCISE_09 ON TradingExcise (VchCode,MCCode,ItemCode,RefNo);
CREATE INDEX TRADINGEXCISE_10 ON TradingExcise (AutoRG23DPageNo,AutoRG23DSrNo);
CREATE INDEX TRADINGEXCISE_11 ON TradingExcise (MCCode,AutoRG23DPageNo,AutoRG23DSrNo);








-- Tran1 definition

-- Drop table

-- DROP TABLE Tran1;

CREATE TABLE Tran1 (
    companyid integer DEFAULT 0,
	VchCode integer DEFAULT 0 NOT NULL,
	VchType smallint DEFAULT 0,
	Date timestamp ,
	StockUpdationDate timestamp ,
	Status smallint DEFAULT 0,
	VchNo text,
	VchSeriesCode integer DEFAULT 0,
	MasterCode1 integer DEFAULT 0,
	MasterCode2 integer DEFAULT 0,
	Stamp integer DEFAULT 0,
	AutoVchNo integer DEFAULT 0,
	CM1 integer DEFAULT 0,
	CM2 integer DEFAULT 0,
	CM3 integer DEFAULT 0,
	CM4 integer DEFAULT 0,
	CM5 integer DEFAULT 0,
	CM6 integer DEFAULT 0,
	FormRecAmt float DEFAULT 0,
	FormIssAmt float DEFAULT 0,
	CurConRate float DEFAULT 0,
	VchAmtBaseCur float DEFAULT 0,
	VchSalePurcAmt float DEFAULT 0,
	ExciseApplicable boolean DEFAULT false,
	ExciseDocName text,
	ExciseValue float DEFAULT 0,
	ExciseType smallint DEFAULT 0,
	ExcisableAmount float DEFAULT 0,
	ExciseRate float DEFAULT 0,
	OrgVchAmtBaseCur float DEFAULT 0,
	TEApplicable boolean DEFAULT false,
	TDSApplicable boolean DEFAULT false,
	FormRecStatus smallint DEFAULT 0,
	FormIssStatus smallint DEFAULT 0,
	ChallanStatus smallint DEFAULT 0,
	STApplicable boolean DEFAULT false,
	STType smallint DEFAULT 0,
	DocPrinted boolean DEFAULT false,
	External boolean DEFAULT false,
	CreatedBy text,
	CreationTime timestamp ,
	AuthorisedBy text,
	AuthorisationTime timestamp ,
	ModifiedBy text,
	ModificationTime timestamp ,
	PriceCategory smallint DEFAULT 0,
	VATInfo boolean DEFAULT false,
	POSEnabled boolean DEFAULT false,
	AutoGeneratedType smallint DEFAULT 0,
	VchCancelled boolean DEFAULT false,
	BrokerageMode smallint DEFAULT 0,
	Brokerage float DEFAULT 0,
	BrokerageAmt float DEFAULT 0,
	TranType smallint DEFAULT 0,
	FreeQtyUsed boolean DEFAULT false,
	Cancelled boolean DEFAULT false,
	D1 float DEFAULT 0,
	ApprovalStatus smallint DEFAULT 0,
	SyncStatus boolean DEFAULT false,
	Source smallint DEFAULT 0,
	AuditStatus smallint DEFAULT 0,
	ExtraExpense float DEFAULT 0,
	ExtraExpenseNar1 text,
	ExtraExpenseNar2 text,
	c1 text,
	Date1 timestamp ,
	Date2 timestamp ,
	I1 smallint DEFAULT 0,
	I2 smallint DEFAULT 0,
	I3 smallint DEFAULT 0,
	I4 smallint DEFAULT 0,
	I5 smallint DEFAULT 0,
	I6 smallint DEFAULT 0,
	I7 smallint DEFAULT 0,
	I8 smallint DEFAULT 0,
	I9 smallint DEFAULT 0,
	I10 smallint DEFAULT 0,
	B1 boolean DEFAULT false,
	TPF1 boolean DEFAULT false,
	TPF2 boolean DEFAULT false,
	RejectionStatus smallint DEFAULT 0,
	L1 integer DEFAULT 0,
	SourceDet text,
	NepaliDate text,
	NepaliFY text,
	CM7 integer DEFAULT 0,
	OldIdentity text,
	PRIMARY KEY (VchCode, companyid)
);
CREATE UNIQUE INDEX SYS_IDX_SYS_PK_12199_12200 ON Tran1 (VchCode, companyid);
CREATE INDEX TRAN1_02 ON Tran1 (MasterCode1);
CREATE INDEX TRAN1_03 ON Tran1 (MasterCode2);
CREATE INDEX TRAN1_19 ON Tran1 (CM5);
CREATE INDEX TRAN1_21 ON Tran1 (Date);
CREATE INDEX TRAN1_22 ON Tran1 (VchType);
CREATE INDEX TRAN1_23 ON Tran1 (VchNo);
CREATE INDEX TRAN1_24 ON Tran1 (VchSeriesCode);
CREATE INDEX TRAN1_26 ON Tran1 (CM1);
CREATE INDEX TRAN1_27 ON Tran1 (CM2);
CREATE INDEX TRAN1_28 ON Tran1 (CM3);
CREATE INDEX TRAN1_29 ON Tran1 (CM4);
CREATE INDEX TRAN1_30 ON Tran1 (AutoGeneratedType);
CREATE INDEX TRAN1_31 ON Tran1 (StockUpdationDate);
CREATE INDEX TRAN1_32 ON Tran1 (SyncStatus);
CREATE INDEX TRAN1_33 ON Tran1 (Source);
CREATE INDEX TRAN1_34 ON Tran1 (CM7);
CREATE INDEX TRAN1_35 ON Tran1 (TranType);
CREATE INDEX TRAN1_62 ON Tran1 (VchType,Date);
CREATE INDEX TRAN1_63 ON Tran1 (VchSeriesCode,AutoVchNo);
CREATE INDEX TRAN1_64 ON Tran1 (VchSeriesCode,Date,VchNo);
CREATE INDEX TRAN1_81 ON Tran1 (VchCode);
CREATE INDEX TRAN1_82 ON Tran1 (Date);




-- Tran2 definition

-- Drop table

-- DROP TABLE Tran2;

CREATE TABLE Tran2 (
    companyid integer DEFAULT 0,
	RecType smallint DEFAULT 0,
	VchCode integer DEFAULT 0,
	MasterCode1 integer DEFAULT 0,
	MasterCode2 integer DEFAULT 0,
	SrNo smallint DEFAULT 0,
	VchType smallint DEFAULT 0,
	Date timestamp ,
	VchNo text,
	VchSeriesCode integer DEFAULT 0,
	Value1 float DEFAULT 0,
	Value2 float DEFAULT 0,
	Value3 float DEFAULT 0,
	Balance1 float DEFAULT 0,
	Balance2 float DEFAULT 0,
	Balance3 float DEFAULT 0,
	ItemBal1 float DEFAULT 0,
	ItemBal2 float DEFAULT 0,
	ItemBal3 float DEFAULT 0,
	CashFlow float DEFAULT 0,
	ShortNar text,
	D1 float DEFAULT 0,
	D2 float DEFAULT 0,
	D3 float DEFAULT 0,
	D4 float DEFAULT 0,
	D5 float DEFAULT 0,
	D6 float DEFAULT 0,
	D7 float DEFAULT 0,
	D8 float DEFAULT 0,
	D9 float DEFAULT 0,
	D10 float DEFAULT 0,
	D11 float DEFAULT 0,
	D12 float DEFAULT 0,
	D13 float DEFAULT 0,
	D14 float DEFAULT 0,
	D15 float DEFAULT 0,
	D16 float DEFAULT 0,
	D17 float DEFAULT 0,
	D18 float DEFAULT 0,
	D19 float DEFAULT 0,
	D20 float DEFAULT 0,
	D21 float DEFAULT 0,
	D22 float DEFAULT 0,
	D23 float DEFAULT 0,
	D24 float DEFAULT 0,
	D25 float DEFAULT 0,
	D26 float DEFAULT 0,
	D27 float DEFAULT 0,
	D28 float DEFAULT 0,
	D29 float DEFAULT 0,
	D30 float DEFAULT 0,
	D31 float DEFAULT 0,
	D32 float DEFAULT 0,
	I1 smallint DEFAULT 0,
	CM1 integer DEFAULT 0,
	CM2 integer DEFAULT 0,
	CM3 integer DEFAULT 0,
	CM4 integer DEFAULT 0,
	CM5 integer DEFAULT 0,
	CM6 integer DEFAULT 0,
	CM7 integer DEFAULT 0,
	CM8 integer DEFAULT 0,
	CM9 integer DEFAULT 0,
	B1 boolean DEFAULT false,
	B2 boolean DEFAULT false,
	B3 boolean DEFAULT false,
	B4 boolean DEFAULT false,
	B5 boolean DEFAULT false,
	B6 boolean DEFAULT false,
	B7 boolean DEFAULT false,
	B8 boolean DEFAULT false,
	ClrDate timestamp ,
	PriceCategory smallint DEFAULT 0,
	CFMode smallint DEFAULT 0,
	C1 text,
	C2 text,
	C3 text,
	TranType smallint DEFAULT 0,
	IsReturnQty boolean DEFAULT false,
	ReconStatus boolean DEFAULT false,
	I2 smallint DEFAULT 0,
	I3 smallint DEFAULT 0,
	I4 smallint DEFAULT 0,
	I5 smallint DEFAULT 0,
	I6 smallint DEFAULT 0,
	I7 smallint DEFAULT 0,
	I8 smallint DEFAULT 0,
	I9 smallint DEFAULT 0,
	I10 smallint DEFAULT 0,
	TrackingStatus smallint DEFAULT 0,
	TrackingNo text,
	PRIMARY KEY (VchCode, MasterCode2, SrNo, companyid)
);
CREATE INDEX TRAN2_01 ON Tran2 (MasterCode1);
CREATE INDEX TRAN2_02 ON Tran2 (MasterCode2);
CREATE INDEX TRAN2_03 ON Tran2 (CM1);
CREATE INDEX TRAN2_08 ON Tran2 (VchCode);
CREATE INDEX TRAN2_31 ON Tran2 (RecType);
CREATE INDEX TRAN2_32 ON Tran2 (VchType);
CREATE INDEX TRAN2_33 ON Tran2 (VchNo);
CREATE INDEX TRAN2_34 ON Tran2 (Date);
CREATE INDEX TRAN2_36 ON Tran2 (VchSeriesCode);
CREATE INDEX TRAN2_38 ON Tran2 (CM2);
CREATE INDEX TRAN2_39 ON Tran2 (CM3);
CREATE INDEX TRAN2_40 ON Tran2 (CM4);
CREATE INDEX TRAN2_41 ON Tran2 (CM5);
CREATE INDEX TRAN2_42 ON Tran2 (D18);
CREATE INDEX TRAN2_43 ON Tran2 (D26);
CREATE INDEX TRAN2_44 ON Tran2 (CM6);
CREATE INDEX TRAN2_45 ON Tran2 (IsReturnQty);
CREATE INDEX TRAN2_46 ON Tran2 (C3);
CREATE INDEX TRAN2_47 ON Tran2 (TrackingNo);
CREATE INDEX TRAN2_48 ON Tran2 (TrackingStatus);
CREATE INDEX TRAN2_49 ON Tran2 (TranType);
CREATE INDEX TRAN2_50 ON Tran2 (CM7);
CREATE INDEX TRAN2_51 ON Tran2 (CM8);
CREATE INDEX TRAN2_52 ON Tran2 (CM9);
CREATE INDEX TRAN2_81 ON Tran2 (MasterCode2);





-- Tran3 definition

-- Drop table

-- DROP TABLE Tran3;

CREATE TABLE Tran3 (
	RefCode integer DEFAULT 0,
	RecType smallint DEFAULT 0,
	Method smallint DEFAULT 0,
	VchCode integer DEFAULT 0,
	VchType smallint DEFAULT 0,
	MasterCode1 integer DEFAULT 0,
	MasterCode2 integer DEFAULT 0,
	RefGrp integer DEFAULT 0,
	SrNo smallint DEFAULT 0,
	Date timestamp ,
	DueDate timestamp ,
	No text,
	Status smallint DEFAULT 0,
	Type smallint DEFAULT 0,
	BrokerCode integer DEFAULT 0,
	Value1 float DEFAULT 0,
	Value2 float DEFAULT 0,
	Value3 float DEFAULT 0,
	Balance1 float DEFAULT 0,
	Balance2 float DEFAULT 0,
	Balance3 float DEFAULT 0,
	ItemSrNo smallint DEFAULT 0,
	MfgDate timestamp ,
	TranType smallint DEFAULT 0,
	CM1 integer DEFAULT 0,
	CM2 integer DEFAULT 0,
	ApprovalStatus smallint DEFAULT 0,
	NewRefAmount float DEFAULT 0,
	Narration text,
	BranchCode integer DEFAULT 0
);
CREATE INDEX TRAN3_04 ON Tran3 (MasterCode1);
CREATE INDEX TRAN3_05 ON Tran3 (MasterCode2);
CREATE INDEX TRAN3_09 ON Tran3 (RefGrp);
CREATE INDEX TRAN3_20 ON Tran3 (SrNo);
CREATE INDEX TRAN3_21 ON Tran3 (Date);
CREATE INDEX TRAN3_22 ON Tran3 (VchType);
CREATE INDEX TRAN3_23 ON Tran3 (VchCode);
CREATE INDEX TRAN3_24 ON Tran3 (RefCode);
CREATE INDEX TRAN3_25 ON Tran3 (RecType);
CREATE INDEX TRAN3_26 ON Tran3 (Type);
CREATE INDEX TRAN3_27 ON Tran3 (Method);
CREATE INDEX TRAN3_28 ON Tran3 (DueDate);
CREATE INDEX TRAN3_29 ON Tran3 (No);
CREATE INDEX TRAN3_31 ON Tran3 (Status);
CREATE INDEX TRAN3_32 ON Tran3 (ApprovalStatus);
CREATE INDEX TRAN3_33 ON Tran3 (TranType);
CREATE INDEX TRAN3_34 ON Tran3 (Value1);
CREATE INDEX TRAN3_61 ON Tran3 (RecType,MasterCode1,MasterCode2,No);
CREATE INDEX TRAN3_62 ON Tran3 (RefCode,Date);
CREATE INDEX TRAN3_81 ON Tran3 (RefCode);






-- Tran4 definition

-- Drop table

-- DROP TABLE Tran4;

CREATE TABLE Tran4 (
	SrNo integer DEFAULT 0,
	MasterCode1 integer DEFAULT 0,
	MasterCode2 integer DEFAULT 0,
	D1 float DEFAULT 0,
	D2 float DEFAULT 0,
	D3 float DEFAULT 0,
	BranchCode integer DEFAULT 0,
	RecType smallint DEFAULT 0
);
CREATE INDEX TRAN4_01 ON Tran4 (MasterCode1,MasterCode2);
CREATE INDEX TRAN4_02 ON Tran4 (MasterCode1,SrNo);
CREATE INDEX TRAN4_03 ON Tran4 (MasterCode2);
CREATE INDEX TRAN4_06 ON Tran4 (BranchCode);
CREATE INDEX TRAN4_07 ON Tran4 (RecType);



-- Tran5 definition

-- Drop table

-- DROP TABLE Tran5;

CREATE TABLE Tran5 (
	VchCode integer DEFAULT 0,
	MasterCode1 integer DEFAULT 0,
	MasterCode2 integer DEFAULT 0,
	SrNo smallint DEFAULT 0,
	VchType smallint DEFAULT 0,
	Date timestamp ,
	VchNo text,
	VchSeriesCode integer DEFAULT 0,
	Value1 float DEFAULT 0,
	Value2 float DEFAULT 0,
	Balance1 float DEFAULT 0,
	Balance2 float DEFAULT 0,
	TranType smallint DEFAULT 0,
	ShortNar text,
	TrackingNo text,
	TrackingStatus smallint DEFAULT 0
);
CREATE INDEX TRAN5_01 ON Tran5 (MasterCode1,Date,VchType,VchNo,VchCode);
CREATE INDEX TRAN5_02 ON Tran5 (VchCode,MasterCode1,TranType,SrNo);
CREATE INDEX TRAN5_03 ON Tran5 (VchCode,TranType,SrNo);
CREATE INDEX TRAN5_04 ON Tran5 (MasterCode1,MasterCode2,Date,VchNo,VchCode);
CREATE INDEX TRAN5_05 ON Tran5 (MasterCode1,VchType,Date,VchNo,VchCode);
CREATE INDEX TRAN5_06 ON Tran5 (MasterCode1,MasterCode2,Value1,Date);
CREATE INDEX TRAN5_07 ON Tran5 (MasterCode2,MasterCode1,Value1,Date);
CREATE INDEX TRAN5_08 ON Tran5 (MasterCode1,VchType,Value1,Date);
CREATE INDEX TRAN5_09 ON Tran5 (VchType,MasterCode1,Value1,Date);
CREATE INDEX TRAN5_10 ON Tran5 (VchCode,MasterCode2,SrNo);





-- Tran6 definition

-- Drop table

-- DROP TABLE Tran6;

CREATE TABLE Tran6 (
	SrNo integer DEFAULT 0,
	MasterCode1 integer DEFAULT 0,
	MasterCode2 integer DEFAULT 0,
	StockType smallint DEFAULT 0,
	D1 float DEFAULT 0,
	D2 float DEFAULT 0,
	D3 float DEFAULT 0
);
CREATE INDEX TRAN6_01 ON Tran6 (MasterCode1,MasterCode2,StockType);
CREATE INDEX TRAN6_02 ON Tran6 (MasterCode1,StockType,SrNo);
CREATE INDEX TRAN6_03 ON Tran6 (MasterCode2);





-- Tran7 definition

-- Drop table

-- DROP TABLE Tran7;

CREATE TABLE Tran7 (
	MasterCode integer DEFAULT 0
);
CREATE INDEX TRAN7_01 ON Tran7 (MasterCode);



-- Tran8 definition

-- Drop table

-- DROP TABLE Tran8;

CREATE TABLE Tran8 (
	VchCode integer DEFAULT 0 NOT NULL,
	VchType smallint DEFAULT 0,
	Date timestamp ,
	FormRecDate timestamp ,
	FormNo text,
	PartyCode integer DEFAULT 0,
	FormCode integer DEFAULT 0,
	Stamp integer DEFAULT 0,
	Nar1 text,
	AutoVchNo integer DEFAULT 0,
	CreatedBy text,
	CreationTime timestamp ,
	AuthorisedBy text,
	AuthorisationTime timestamp ,
	ModifiedBy text,
	ModificationTime timestamp ,
	StateCode smallint DEFAULT 0,
	Series text,
	IssuingOffice text,
	CONSTRAINT SYS_PK_12204 PRIMARY KEY (VchCode)
);
CREATE UNIQUE INDEX SYS_IDX_SYS_PK_12204_12205 ON Tran8 (VchCode);
CREATE INDEX TRAN8_02 ON Tran8 (VchType,Date,FormNo,VchCode);
CREATE INDEX TRAN8_03 ON Tran8 (VchType,FormNo);




-- Tran9 definition

-- Drop table

-- DROP TABLE Tran9;

CREATE TABLE Tran9 (
	VchCode integer DEFAULT 0,
	PartyCode integer DEFAULT 0,
	FormCode integer DEFAULT 0,
	SrNo smallint DEFAULT 0,
	VchType smallint DEFAULT 0,
	Date timestamp ,
	FormNo text,
	BillCode integer DEFAULT 0,
	Amount float DEFAULT 0
);
CREATE INDEX TRAN9_01 ON Tran9 (VchCode,SrNo);
CREATE INDEX TRAN9_02 ON Tran9 (VchType,BillCode);





-- Tran10 definition

-- Drop table

-- DROP TABLE Tran10;

CREATE TABLE Tran10 (
	RecType smallint DEFAULT 0,
	VchType smallint DEFAULT 0,
	I1 smallint DEFAULT 0,
	I2 smallint DEFAULT 0,
	I3 smallint DEFAULT 0,
	I4 smallint DEFAULT 0,
	SrNo smallint DEFAULT 0,
	Mastercode1 integer DEFAULT 0,
	MasterCode2 integer DEFAULT 0,
	D1 float DEFAULT 0,
	D2 float DEFAULT 0,
	D3 float DEFAULT 0,
	D4 float DEFAULT 0,
	D5 float DEFAULT 0,
	D6 float DEFAULT 0,
	D7 float DEFAULT 0,
	D8 float DEFAULT 0,
	D9 float DEFAULT 0,
	D10 float DEFAULT 0,
	C1 text,
	C2 text,
	C3 text,
	C4 text,
	C5 text,
	C6 text,
	C7 text,
	C8 text,
	C9 text,
	C10 text,
	Date timestamp ,
	MasterCode3 integer DEFAULT 0,
	B1 boolean DEFAULT false,
	B2 boolean DEFAULT false,
	B3 boolean DEFAULT false
);
CREATE INDEX TRAN10_01 ON Tran10 (Mastercode1,MasterCode2);
CREATE INDEX TRAN10_02 ON Tran10 (MasterCode2);
CREATE INDEX TRAN10_03 ON Tran10 (VchType,RecType,Mastercode1,SrNo);
CREATE INDEX TRAN10_04 ON Tran10 (C1);
CREATE INDEX TRAN10_05 ON Tran10 (MasterCode3);
CREATE INDEX TRAN10_06 ON Tran10 (Date);
CREATE INDEX TRAN10_07 ON Tran10 (Date);
CREATE INDEX TRAN10_08 ON Tran10 (RecType);


-- Tran11 definition

-- Drop table

-- DROP TABLE Tran11;

CREATE TABLE Tran11 (
	RecType smallint DEFAULT 0,
	TranType smallint DEFAULT 0,
	VchCode integer DEFAULT 0,
	MasterCode1 integer DEFAULT 0,
	MasterCode2 integer DEFAULT 0,
	SrNo smallint DEFAULT 0,
	VchType smallint DEFAULT 0,
	Date timestamp ,
	VchNo text,
	VchSeriesCode integer DEFAULT 0,
	ShortNar text,
	I1 smallint DEFAULT 0,
	I2 smallint DEFAULT 0,
	B1 boolean DEFAULT false,
	CM1 integer DEFAULT 0,
	CM2 integer DEFAULT 0,
	CM3 integer DEFAULT 0,
	CM4 integer DEFAULT 0,
	CM5 integer DEFAULT 0,
	CM6 integer DEFAULT 0,
	CM7 integer DEFAULT 0,
	CM8 integer DEFAULT 0,
	Date1 timestamp ,
	Date2 timestamp ,
	Date3 timestamp ,
	Date4 timestamp ,
	Date5 timestamp ,
	C1 text,
	C2 text,
	M1 text,
	M2 text
);
CREATE INDEX TRAN11_01 ON Tran11 (MasterCode1);
CREATE INDEX TRAN11_02 ON Tran11 (C1);
CREATE INDEX TRAN11_03 ON Tran11 (Date);
CREATE INDEX TRAN11_04 ON Tran11 (CM3);
CREATE INDEX TRAN11_05 ON Tran11 (TranType);
CREATE INDEX TRAN11_06 ON Tran11 (VchType);
CREATE INDEX TRAN11_07 ON Tran11 (RecType);




-- Tran12 definition

-- Drop table

-- DROP TABLE Tran12;

CREATE TABLE Tran12 (
	VchCode integer DEFAULT 0,
	Date timestamp ,
	UserName text
);
CREATE INDEX TRAN12_01 ON Tran12 (VchCode);
CREATE INDEX TRAN12_02 ON Tran12 (Date);




-- VATInfo definition

-- Drop table

-- DROP TABLE VATInfo;

CREATE TABLE VATInfo (
	Date timestamp ,
	Amount float DEFAULT 0,
	RecType smallint DEFAULT 0,
	Type smallint DEFAULT 0,
	SrNo smallint DEFAULT 0,
	Description text,
	VchCode integer DEFAULT 0,
	ChallanNo text,
	ChallanDate timestamp ,
	ChequeNo text,
	ChequeDate timestamp ,
	BankName text,
	BankCode text,
	Interest float DEFAULT 0,
	Penalty float DEFAULT 0,
	BankAcType text,
	BankAcNo text,
	SurchargeAmt float DEFAULT 0,
	SaleAmt float DEFAULT 0,
	TaxPercent float DEFAULT 0,
	SurchargePercent float DEFAULT 0
);
CREATE INDEX VATINFO_01 ON VATInfo (Date);
CREATE INDEX VATINFO_02 ON VATInfo (VchCode);



-- VchOtherInfo definition

-- Drop table

-- DROP TABLE VchOtherInfo;

CREATE TABLE VchOtherInfo (
	VchCode integer DEFAULT 0,
	OF1 text,
	OF2 text,
	OF3 text,
	OF4 text,
	OF5 text,
	OF6 text,
	OF7 text,
	OF8 text,
	OF9 text,
	OF10 text,
	Transport text,
	Station text,
	GrNo text,
	VehicleNo text,
	ItemDesc text,
	Form31No text,
	Form31IssuedOn text,
	TotalQty text,
	PurchaseBillNo text,
	PurchaseBillDate text,
	Narration1 text,
	Narration2 text,
	InvoicePrepTime text,
	GoodsRemovalTime text,
	GrDate timestamp ,
	VchNotes text,
	I1 smallint DEFAULT 0,
	OF11 text,
	OF12 text,
	OF13 text,
	OF14 text,
	OF15 text,
	OF16 text,
	OF17 text,
	OF18 text,
	OF19 text,
	OF20 text
);
CREATE INDEX VCHOTHERINFO_01 ON VchOtherInfo (VchCode);




-- VchTemplate definition

-- Drop table

-- DROP TABLE VchTemplate;

CREATE TABLE VchTemplate (
	VchCode integer DEFAULT 0,
	TemplateName text
);
CREATE INDEX VCHTEMPLATE_01 ON VchTemplate (VchCode);
CREATE INDEX VCHTEMPLATE_02 ON VchTemplate (TemplateName);




-- VchTempTagging definition

-- Drop table

-- DROP TABLE VchTempTagging;

CREATE TABLE VchTempTagging (
	MasterCode integer DEFAULT 0,
	VchType smallint DEFAULT 0,
	TemplateVchCode integer DEFAULT 0,
	B1 boolean DEFAULT false,
	B2 boolean DEFAULT false,
	B3 boolean DEFAULT false,
	B4 boolean DEFAULT false,
	B5 boolean DEFAULT false,
	I1 smallint DEFAULT 0,
	I2 smallint DEFAULT 0,
	MasterType smallint DEFAULT 0
);
CREATE INDEX VCHTEMPTAGGING_01 ON VchTempTagging (MasterCode,VchType);
CREATE INDEX VCHTEMPTAGGING_02 ON VchTempTagging (MasterType,VchType);





-- VchVATSum definition

-- Drop table

-- DROP TABLE VchVATSum;

CREATE TABLE VchVATSum (
	VchCode integer DEFAULT 0,
	SaleAmt float DEFAULT 0,
	TaxRate float DEFAULT 0,
	TaxAmt float DEFAULT 0,
	SurchargeRate float DEFAULT 0,
	SurchargeAmt float DEFAULT 0,
	TaxType smallint DEFAULT 0,
	ActualSaleAmt float DEFAULT 0,
	TaxOnMRP boolean DEFAULT false
);
CREATE INDEX VCHVATSUM_01 ON VchVATSum (VchCode);




-- VchVATSumItemWise definition

-- Drop table

-- DROP TABLE VchVATSumItemWise;

CREATE TABLE VchVATSumItemWise (
	ItemSrNo smallint DEFAULT 0,
	ItemCode integer DEFAULT 0,
	VchCode integer DEFAULT 0,
	SaleAmt float DEFAULT 0,
	TaxRate float DEFAULT 0,
	TaxAmt float DEFAULT 0,
	SurchargeRate float DEFAULT 0,
	SurchargeAmt float DEFAULT 0,
	TaxType smallint DEFAULT 0,
	ActualSaleAmt float DEFAULT 0,
	TaxOnMRP boolean DEFAULT false
);
CREATE INDEX VCHVATSUMITEMWISE_01 ON VchVATSumItemWise (VchCode,ItemSrNo);
CREATE INDEX VCHVATSUMITEMWISE_02 ON VchVATSumItemWise (ItemCode);






"""