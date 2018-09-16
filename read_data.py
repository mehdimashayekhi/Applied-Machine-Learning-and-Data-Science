import numpy as np
import pandas as pd



def data_cleaning():
    # this is for cleaning utf csv
    test_df = pd.read_csv('test_09_14_18.csv')
    print (test_df.head())
    newDF = pd.DataFrame()
    i=0
    for col in test_df:
    	if i==0:
    		newDF['text']=test_df[col]
    		i+=1
    	else:
    		newDF['intent']=test_df[col]


    assert "text" in newDF and "intent" in newDF, "The test file must contain two columns 'text' and 'intent'"

    # print("mehdiiiiiiiii")
    print (newDF['intent'])



    for column in newDF.columns:
        for idx in newDF[column].index:
            x = newDF.get_value(idx,column)
            try:
                x = unicode(x.encode('utf-8','ignore'),errors ='ignore') if type(x) == unicode else unicode(str(x),errors='ignore')
                newDF.set_value(idx,column,x)
            except Exception:
                print 'encoding error: {0} {1}'.format(idx,column)
                newDF.set_value(idx,column,'')
                continue
    # print("mehdiiiiiiiii")
    print (newDF['intent'])
    newDF.to_csv('test_09_14_18_1.csv', encoding='utf-8', errors='replace', index=False)



def data_preparation():
    df = pd.read_excel('TEST.xlsx', sheetname='Sheet1')
    # print (df.head())
    print df['Position 1']
    newDF = pd.DataFrame()
    text =[]
    intent=[]
    for index, row in df.iterrows():
        if not pd.isnull(df.at[index,'Position 1']):
            value = row['Position 1']
            if str(value).isdigit():
                value = "TOPIC-"+str(value)
            text.append(row['TEXT'])
            intent.append(value)
        if not pd.isnull(df.at[index,'Position 2']):
            value = row['Position 2']
            if str(value).isdigit():
                value = "TOPIC-"+str(value)
            text.append(row['TEXT'])
            intent.append(value)
        if not pd.isnull(df.at[index,'Position 3']):
            value = row['Position 3']
            if str(value).isdigit():
                value = "TOPIC-"+str(value)
            text.append(row['TEXT'])
            intent.append(value)

    newDF['text']=text
    newDF['intent']=intent

    print (newDF['text'],newDF['intent'])

    newDF.to_csv('processed.csv', encoding='utf-8', errors='replace', index=False)


if __name__ == '__main__':
    # data_cleaning()
    data_preparation()



# import csv
# with open(r"lucine.csv", 'rb') as f:
#     reader = csv.reader(f)
#     linenumber = 1
#     try:
#         for row in reader:
#             linenumber += 1
#             print row
#     except Exception as e:
#         print (("Error line %d: %s %s" % (linenumber, str(type(e)), e.message)))