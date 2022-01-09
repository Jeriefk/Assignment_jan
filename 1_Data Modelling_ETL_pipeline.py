import psycopg2
import pandas as pd
conn = psycopg2.connect(dbname="order_db", user="postgres", port=5432)
cursor = conn.cursor()

def overall_report_monthly():
    overall_monthly_rpt = "select * from monthly_rpt;"
    cursor.execute(overall_monthly_rpt)
    overall_monthly_rpt_var = cursor.fetchall()
    return overall_monthly_rpt_var
def overall_status_category():
    status_category_rpt="select * from monthly_status_category_rpt;"
    cursor.execute(status_category_rpt)
    status_category_rpt_var = cursor.fetchall()
    return status_category_rpt_var
if __name__ == "__main__":
    overall_report_df=pd.DataFrame(overall_report_monthly())
    overall_status_category_df=pd.DataFrame(overall_status_category())
    print("Monthly report")
    print(overall_report_df)
    print("Report at status and catgeory level")
    print(overall_status_category_df)
