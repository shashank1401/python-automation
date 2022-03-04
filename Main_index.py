from selenium import webdriver
import pickle
import time
import pandas as pd
import re
from selenium.webdriver.common.by import By


class Automation_Ticket(object):
    def __init__(self):
        self.Driver_Ticket=webdriver.Chrome("./WEB_DRIVER/chromedriver.exe")
        self.Driver_Ticket.maximize_window()
        self.Driver_Ticket.get("http://dms-siel.com/SMT/Login")
        self.flag=0
        self.flag1=0
        time.sleep(30)
    def DashBoard(self):
        Element2=self.Driver_Ticket.find_element_by_xpath("//h2[@class='menuMainA']")
        Element2.click()
        # exit()

        Element3=self.Driver_Ticket.find_element_by_link_text('Dashboard')

        Element3.click()
        time.sleep(3)
    def Click_Ticket_Request(self):

        Element2=self.Driver_Ticket.find_element_by_xpath("//h2[@class='menuMainA']")
        Element2.click()
        time.sleep(3)
        # zmdi zmdi-hc-1x zmdi-tv-list floatRight
        Element3=self.Driver_Ticket.find_element_by_xpath("//i[@class='zmdi zmdi-hc-1x zmdi-tv-list floatRight']")

        Element3.click()
        time.sleep(3)
        # exit()

        # zmdi zmdi-folder zmdiMenu floatRight
        Ticket_Request=self.Driver_Ticket.find_element_by_xpath("//i[@class='zmdi zmdi-ticket-star zmdiMenu floatRight']")

        # Element3.click()
        # Ticket_Request=self.Driver_Ticket.find_element_by_link_text('Ticket Request')
        self.Driver_Ticket.implicitly_wait(3)
        Ticket_Request.click()
    def Customer_Name(self,CustomerName):
        print("+aaaa++++aaa+++++++")
        time.sleep(2)
        print(CustomerName)
        self.flag=0
        Element1 = self.Driver_Ticket.find_element_by_id('ddlSearchby')
        for option in Element1.find_elements_by_tag_name('option'):
            if option.text == 'Customer Name':
                option.click()
        time.sleep(2)
        Input_Element = self.Driver_Ticket.find_element_by_id("txtCustomerName")
        Input_Element.send_keys(CustomerName)
        time.sleep(4)
        try:
            Element2= self.Driver_Ticket.find_element_by_class_name("suggest")
            print("++++++++++++++++++++++++")
            print(Element2)
            Element2.click()
            time.sleep(3)
            self.flag=1
            print("********************")
            Element2=self.Driver_Ticket.find_element_by_xpath("//button[@class='btn-dark tktRqst float-lg-right']")
            time.sleep(3)
            Element2.click()
            time.sleep(3)
        except Exception as e:
            # continue
            print(e)
        if self.flag==0:
            print("++++++++++++++++++++++++++++++++++++++++++++++++++")
            print("dadadasdasdasdas")
            file1.write("\n")
            return "CustomerNotFound"
        else:
            print("ddddddddddddddddddddddddddddddddddddddddddddddddddddddddd")
            # exit()
        # exit()
    def Service_Option(self):
        Element1 = self.Driver_Ticket.find_element_by_id('ddlRequestType')
        for option in Element1.find_elements_by_tag_name('option'):
            if option.text == 'Service':
                option.click()
                time.sleep(2)

    def Priority_Option(self):
        Element1 = self.Driver_Ticket.find_element_by_id('ddlPriority')
        for option in Element1.find_elements_by_tag_name('option'):
            if option.text == 'S3 ( <5% Users Impacted )':
                option.click()
                time.sleep(2)

    def Communication_Mode(self):
        Element1 = self.Driver_Ticket.find_element_by_id('ddlModeOfCommunication')
        for option in Element1.find_elements_by_tag_name('option'):
            if option.text == 'Web':
                option.click()
                time.sleep(2)

    def Module_Select(self,Type):
        Element1 = self.Driver_Ticket.find_element_by_id('dvProduct')
        # dvProduct
        flag_1=''
        try:
            for option in Element1.find_elements_by_tag_name('option'):
                if option.text == 'SeWIMS':
                    option.click()
                    time.sleep(3)
        except Exception as e:
            print("5++++++5555++++++++++++")
            flag_1='TrueVlaue'
            # return 'customernamewrongs'
        if flag_1=='TrueVlaue':
            return 'customernamewrongs'
        Element1 = self.Driver_Ticket.find_element_by_id('ddlWorkGroup')
        # dvProduct
        for option in Element1.find_elements_by_tag_name('option'):
            if option.text == 'EInvoice-EWayBill':
                option.click()
                time.sleep(1)


        Element1 = self.Driver_Ticket.find_element_by_id('ddlModule')
        # dvProduct
        for option in Element1.find_elements_by_tag_name('option'):
            if option.text == Type:
                option.click()
                time.sleep(3)
        # Element1 = self.Driver_Ticket.find_element_by_id('dvProduct')
        # # dvProduct
        # for option in Element1.find_elements_by_tag_name('option'):
        #     if option.text == 'SeWIMS':
        #         option.click()
        #         time.sleep(3)

    def Catalog_Select(self,Catalog):
        time.sleep(2)
        self.flag1=0
        try:

            Element1 = self.Driver_Ticket.find_element_by_id('ddlSymtoms1')
            for option in Element1.find_elements_by_tag_name('option'):
        # ['Data Mismatch','Data not interfaced for EPE/ASN','Email Not Received','HSN Update','Invoice Not showing','N/w Upload not working','Others','PDF not generating','Pincode Update','Report generation error','Report Not Showing','Searching Not Working','Slowness']
                if option.text == Catalog:
                    option.click()
                    time.sleep(2)

            Element1 = self.Driver_Ticket.find_element_by_id('ddlSymtoms2')
            for option in Element1.find_elements_by_tag_name('option'):
        # ['Data Mismatch','Data not interfaced for EPE/ASN','Email Not Received','HSN Update','Invoice Not showing','N/w Upload not working','Others','PDF not generating','Pincode Update','Report generation error','Report Not Showing','Searching Not Working','Slowness']
                if option.text == 'Others':
                    option.click()
                    time.sleep(2)

            Element1 = self.Driver_Ticket.find_element_by_id('ddlSymtoms3')
            for option in Element1.find_elements_by_tag_name('option'):
        # ['Data Mismatch','Data not interfaced for EPE/ASN','Email Not Received','HSN Update','Invoice Not showing','N/w Upload not working','Others','PDF not generating','Pincode Update','Report generation error','Report Not Showing','Searching Not Working','Slowness']
                if option.text == 'Others':
                    option.click()
                    time.sleep(2)
            self.flag1=1
        except Exception as e:
            print(e)
        if self.flag1==0:
            return 'catalogerror'

    def Description_Add(self,Description):
        Element1 = self.Driver_Ticket.find_element_by_id("txtRequestDescription")
        Element1.send_keys(Description)

    def Submit_Button(self):

        # Element1 = self.Driver_Ticket.find_element_by_id("btn-submit text-white")
        # Element1.click()

        Element1=self.Driver_Ticket.find_element_by_xpath("//a[@class='btn-submit text-white']")
        fladd=1
        try:
            Element1.click()
            time.sleep(6)
        except Exception as e:
            fladd=0
            print(e)
        if fladd==0:
            return 'Otheruser'
        # Ticketvalue =self.Driver_Ticket.find_element_by_xpath("//p[@class='lead text-muted']").text
        # print(Ticketvalue)
        # Ticketnumber1=Ticketvalue.split('-')



        Element2=self.Driver_Ticket.find_element_by_xpath("//button[@class='confirm btn btn-lg btn-primary']")
        Element2.click()
        time.sleep(2)
        # Element3=self.Driver_Ticket.find_element_by_link_text('Dashboard')
        # Element3=self.Driver_Ticket.find_element_by_xpath("//i[@class='zmdi zmdi-view-dashboard']")

        # Element3.click()
        # time.sleep(2)
        # Element4=self.Driver_Ticket.find_element_by_link_text(Ticketnumber1[1])
        # Element4.click()


    def Ticket_Value(self):
        #lead text-muted
        #http://dms-siel.com/SMT/CustomerSearch/CustomerRequest
        #confirm btn btn-lg btn-primary     button class
        time.sleep(1)
        Ticket_Number=self.Driver_Ticket.find_element_by_id("callRequestNO").text
        print(Ticket_Number)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
        return Ticket_Number
    def Repair_Description(self,R_Descritpion):
        print(R_Descritpion)
        Element1 = self.Driver_Ticket.find_element_by_id("txtAgentRemarks")
        Element1.send_keys(R_Descritpion)

    def Change_Status(self):
        Element1 = self.Driver_Ticket.find_element_by_id('ddlStatus1')
        for option in Element1.find_elements_by_tag_name('option'):
            if option.text == 'Resolved':
                option.click()
                time.sleep(1)


    def Agent_Name(self):
        Element1 = self.Driver_Ticket.find_element_by_id("txtAgentRemarks1")
        Element1.send_keys('Shashank')
        time.sleep(1)
    def Time_Spent(self,TimeSpents):
        print(TimeSpents)
        Element1 = self.Driver_Ticket.find_element_by_id("txtSpendTimeInMinute")
        Element1.send_keys('2')
        time.sleep(1)

    def Final_Submit(self):
        Element1=self.Driver_Ticket.find_element_by_xpath("//a[@class='btn-submit text-white']")
        Element1.click()
        # confirm btn btn-lg btn-primary
        time.sleep(2)
    def Final_Ok(self):
        Element1=self.Driver_Ticket.find_element_by_xpath("//button[@class='confirm btn btn-lg btn-primary']")
        Element1.click()
        time.sleep(1)

        #callRequestNO  ticket value by name   btn-submit text-white

        #txtAgentRemarks   update value solution


        #ddlStatus1  ,opion Resolved

        #txtAgentRemarks1   value mukesh vishwas

if __name__ == '__main__':
    Ticket_Object=Automation_Ticket()
    Ticket_Object.Click_Ticket_Request()
    file1 = open("my.txt","a+",encoding="utf-8")

    Data_Frame=pd.read_csv('./CSV_FOLDER/Ticket.csv',delimiter=',')
    for row in range(len(Data_Frame.index)):
        file1.write("\n")
        file1.write(Data_Frame['Issue'][row])
        # try:
        #     file1.write(Data_Frame['Issue'][row])
        # except Exception as e:
        #     print(row)
        #     print(e)
            #exit()
        file1.write("-----")
        if row>0:
            # Ticket_Object.DashBoard()
            Ticket_Object.Click_Ticket_Request()
        CustomerName=Data_Frame['Requester'][row]
        Module=Data_Frame['System'][row]
        Time_Spent_value=Data_Frame['Spent time'][row]
        if Module=='E-way':
            Module='Eway_Sales'
        else:
            Module='Einvoice_Sales'
        Catalog= Data_Frame['Issue'][row]
        Match_Catalog1=re.search(r'\baddress\b',Catalog.lower())
        Match_Catalog2=re.search(r'\bupdate\b',Catalog.lower())
        Match_Catalog3=re.search(r'\bhsn\b',Catalog.lower())
        Match_Catalog4=re.search(r'\bpincode\b',Catalog.lower())
        Match_Catalog5=re.search(r'\binvoice\b',Catalog.lower())
        Match_Catalog6=re.search(r'\bshowing\b',Catalog.lower())

        if Match_Catalog1 and Match_Catalog2 :
            Catalog='PDF not generating'
        elif Match_Catalog3 and Match_Catalog2 :
            Catalog='HSN Update'
        elif Match_Catalog4 and Match_Catalog2 :
            Catalog='Pincode Update'
        elif Match_Catalog5 and Match_Catalog6 :
            Catalog='Invoice Not showing'
        else:
            Catalog='PDF not generating'
        Description=Data_Frame['Issue'][row]
        R_Description=Data_Frame['Solution'][row]
        aa=Ticket_Object.Customer_Name(CustomerName)
        if aa=='CustomerNotFound':
            continue
        Ticket_Object.Service_Option()
        Ticket_Object.Priority_Option()
        Ticket_Object.Communication_Mode()
        rr=Ticket_Object.Module_Select(Module)
        if rr=='customernamewrongs':
            continue
        catalogerrors=Ticket_Object.Catalog_Select(Catalog)
        if catalogerrors=='catalogerror':
            continue
        Ticket_Object.Description_Add(Description)
        variabe_otheruser=Ticket_Object.Submit_Button()
        if variabe_otheruser=='otheruser':
            continue


        # Ticket_Number=Ticket_Object.Ticket_Value()
        # print(Ticket_Number)

        Ticket_Object.Change_Status()
        time.sleep(1)
        Ticket_Number=Ticket_Object.Ticket_Value()
        try:
            file1.write(Ticket_Number)
            file1.write(",")
            file1.write("\n")
        except Exception as e:
            print(e)
        Data_Frame['Helpdesk Ticket No. '][row]=Ticket_Number
        Ticket_Object.Repair_Description(R_Description)
        # Ticket_Object.Change_Status()
        Ticket_Object.Time_Spent(Time_Spent_value)
        Ticket_Object.Agent_Name()
        Ticket_Object.Final_Submit()
        Ticket_Object.Final_Ok()
    Data_Frame.to_csv('./csss.csv',index=False)
    file1.close()
    exit()
        #btn-submit text-white class button

        # exit()
