import psycopg2
import pandas as pd
conn = psycopg2.connect(dbname="dbname", user="postgres", port=5432)
curs = conn.cursor()

def overall_report_monthly():
    overall_monthly_report = "select * from monthly_rpt;"
    curs.execute(overall_monthly_report)
    overall_monthly_report_var = curs.fetchall()
    return overall_monthly_report_var
def overall_status_category():
    rpt_status_category="select * from monthly_status_category_rpt;"
    curs.execute(rpt_status_category)
    rpt_status_category_var = curs.fetchall()
    return rpt_status_category_var
if __name__ == "__main__":
    overall_report_df=pd.DataFrame(overall_report_monthly())
    overall_status_category_df=pd.DataFrame(overall_status_category())
    print("Monthly report")
    print(overall_report_df)
    print("Report at status and catgeory level")
    print(overall_status_category_df)
