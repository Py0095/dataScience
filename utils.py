from datetime import datetime
import pandas as pd


file = (r'C:\Users\py0095\Desktop\workPlace\intra\company.csv')


def clean_data(file):
    # read data
    df = pd.read_csv(file).dropna()
    # transform data
    df['salary'] = df['salary'].str.replace('K', '000').str.replace(',', '')
    df['salary'] = df['salary'].astype(float)

    df['gender'] =df['gender'].replace({'Male':'M','Female':'F'},regex=True)

    df['years_at_company'] = df['years_at_company'].replace('years','',regex=True).astype(int)

    # add a new colon
    df['last_promotion_year'] = pd.to_datetime(df['last_promotion_year'], format='%Y')
    current_year = datetime.now().year


    df['years_since_last_promotion'] = current_year - df['last_promotion_year'].dt.year

    formats = ['%d-%b-%Y','%d-%m-%Y','%d-%b-%y','%d-%m-%y']
    # convert date
    def conv(x,formats):
        for f in formats:
            try:
                return pd.to_datetime(x,format=f)
            except:
                pass

    df['hired_date'] = df['hired_date'].apply(lambda x:conv(x,formats)).dt.strftime('%d-%m-%Y')

    data_clean = df.dropna()

    return data_clean



def demographical_analiz(df):
    # Repatisyon chak anplwaye nan chak depatman.
    rep_employe = df['department'].value_counts()
    # Repatisyon pa sèks nan chak depatman.
    rep_seks = df.groupby(['department','gender']).size().unstack()
    # Mwayèn laj anplwaye yo pou chak depatman.
    mwayen_laj = df.groupby('department')['age'].mean()
    return rep_employe, rep_seks, mwayen_laj


def salarial_analiz(df):
    # Mwayèn salè anplwaye yo pou chak depatman.
    mwayen_salè = df.groupby('department')['salary'].mean()
    # Satisfaksyon travay sou chak depatman
    sat_travay_dept = df.groupby('department')['job_satisfaction'].mean()
    return mwayen_salè, sat_travay_dept

def pwomo_educational_analiz(df):
    mwayen_tan_pwomosyon = df.groupby('department')['years_since_last_promotion'].mean().astype(int)
    # Bay mwayèn salè ki ekziste an fonksyon de nivo edikasyon anplwaye yo (Bachelor, Master)
    mwayen_salè_edikasyon = df.groupby('education_level')['salary'].mean()
    return mwayen_tan_pwomosyon, mwayen_salè_edikasyon



# getting clean data
df = clean_data(file)

print(df)


# demographical analiz

print('------------------------------- demographical analiz -------------------------------')


rep_employe, rep_seks, mwayen_laj = demographical_analiz(df)

print('Repatisyon chak anplwaye nan chak depatman')
print(rep_employe)
print('-------------------------------------------')
print('-------------------------------------------')
print('-------------------------------------------')
print('Repatisyon pa sèks nan chak depatman')
print(rep_seks)
print('-------------------------------------------')
print('-------------------------------------------')
print('-------------------------------------------')
print('Mwayèn laj anplwaye yo pou chak depatman')
print('-------------------------------------------')
print('-------------------------------------------')
print('-------------------------------------------')
print(mwayen_laj)



# Kesyon sou Salè
print('------------------------------- Kesyon sou Salè -------------------------------')

mwayen_salè, sat_travay_dept = salarial_analiz(df)
print('Mwayèn salè nan chak depatman')
print(mwayen_salè)
print('-------------------------------------------')
print('-------------------------------------------')
print('-------------------------------------------')
print('Satisfaksyon travay sou chak depatman') 
print(sat_travay_dept)


# Kesyon sou Pwomosyon ak Edikasyon

print('------------------------------- Kesyon sou Pwomosyon ak Edikasyon -------------------------------')

mwayen_tan_pwomosyon, mwayen_salè_edikasyon= pwomo_educational_analiz(df)
print("mwayèn tan ki genyen depi dènye fwa konpayi a te bay yon pwomosyon nan chak depatman?")
print(mwayen_tan_pwomosyon)
print('-------------------------------------------')
print('-------------------------------------------')
print('-------------------------------------------')
print('Bay mwayèn salè ki ekziste an fonksyon de nivo edikasyon anplwaye yo (Bachelor, Master)')
print(mwayen_salè_edikasyon)




