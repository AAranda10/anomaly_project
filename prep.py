import pandas as pd
import acquire


def prep_curriculum_data():
    df = acquire.merge_data()
    df.index = pd.to_datetime(df.date + " " + df.time)
    df = df.drop(columns = {'date', 'time'})
    df['cohort_id'] = df.cohort_id.fillna(0)
    df['name'] = df.name.fillna('Unknown')
    df['start_date'] = df.start_date.fillna('2000-01-01')
    df['end_date'] = df.end_date.fillna('3000-01-01')
    df['program_id'] = df.program_id.fillna(0)
    df['conv_ip'] = df.ip.str.replace('.', '').astype(float)
    df = df[df.page_viewed.str.contains('jpeg') != True]
    df = df[df.page_viewed.str.contains('json') != True]
    df = df[df.page_viewed.str.contains('jpg') != True]
    df = df[df.page_viewed.str.contains('appendix') != True]
    df = df[df.page_viewed.str.contains('Appendix') != True]
    df = df[df.page_viewed != '/']
    df = df[df.page_viewed != 'toc']
    return df

