import psycopg2
import pandas as pd
conn = psycopg2.connect(dbname="dbname", user="postgres", port=5432)
curs = conn.cursor()

def overall_report_monthly():
    overall_monthly_report = "select extract(year from creation_date) yr,extract(month from creation_date) mn,count(order_id) total_orders,sum(order_value)  from orders group by 1,2;"
    curs.execute(overall_monthly_report)
    overall_monthly_report_var = curs.fetchall()
    return overall_monthly_report_var
def overall_status_category():
    rpt_status_category="select extract(year from creation_date) yr,extract(month from creation_date) mn,status,category,count(order_id) total_orders,sum(order_value)  from orders a left join Order_status b on a.status_id=b.status_code left join category c on a.category_id=c.id group by 1,2,3,4;"
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
