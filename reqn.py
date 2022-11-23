import requests
import json

url = "http://localhost:9001/evaluator/flow/v1/flow-4259844136?tableSuffix=trial"

payload = json.dumps({
  "values": {
    "input": {
      "age": 23,
      "gender": "male",
      "work": 984859123,
      "application_id": 1234,
      "applicant_name": "Prakash Laxkar",
      "cibil": {
        "_id": {
          "oid": "60549596af82eb0a0efb4171"
        },
        "user_id": 23468,
        "updated_at": {
          "date": "2021-03-19T12:14:14.902Z"
        },
        "created_at": {
          "date": "2021-03-19T12:14:14.237Z"
        },
        "user_names": [
          {
            "_id": {
              "oid": "60549596af82eb0a0efb4173"
            },
            "_type": "UserName",
            "capture_date": {
              "date": "2021-03-19T00:00:00.000Z"
            },
            "source": "cibil",
            "name1": "MR GYANENDRA KESHERWANI",
            "gender": "2",
            "dob": {
              "date": "1978-10-14T00:00:00.000Z"
            }
          }
        ],
        "user_identifications": [
          {
            "_id": {
              "oid": "60549596af82eb0a0efb4174"
            },
            "_type": "UserIdentification",
            "capture_date": {
              "date": "2021-03-19T00:00:00.000Z"
            },
            "source": "cibil",
            "id_type_code": "01",
            "id_number": "AWAPK0882E"
          }
        ],
        "user_phones": [
          {
            "_id": {
              "oid": "60549596af82eb0a0efb4177"
            },
            "_type": "UserPhone",
            "capture_date": {
              "date": "2021-03-19T00:00:00.000Z"
            },
            "source": "cibil",
            "number": "7974520464",
            "phone_type_code": "01"
          }
        ],
        "user_employments": [
          {
            "_id": {
              "oid": "60549596af82eb0a0efb417b"
            },
            "_type": "UserEmployment",
            "capture_date": {
              "date": "2021-03-19T00:00:00.000Z"
            },
            "source": "cibil",
            "account_type_code": "10",
            "report_date": {
              "date": "2021-03-12T00:00:00.000Z"
            },
            "occupation_code": "03"
          }
        ],
        "user_scores": [
          {
            "_id": {
              "oid": "60549596af82eb0a0efb417c"
            },
            "_type": "UserScore",
            "capture_date": {
              "date": "2021-03-19T00:00:00.000Z"
            },
            "source": "cibil",
            "score_name": "CIBILTUSC3",
            "score": 648,
            "report_date": {
              "date": "2021-03-19T00:00:00.000Z"
            },
            "reason_code_1": "03",
            "reason_code_2": "08",
            "reason_code_3": "02",
            "reason_code_4": "07"
          }
        ],
        "user_bureau_addresses": [
          {
            "_id": {
              "oid": "60549596af82eb0a0efb4189"
            },
            "_type": "UserAccount",
            "capture_date": {
              "date": "2021-03-19T00:00:00.000Z"
            },
            "source": "cibil",
            "reporter_name": "NOT DISCLOSED",
            "account_type": "00",
            "ownership_code": "1",
            "open_date": {
              "date": "2020-03-04T00:00:00.000Z"
            },
            "last_payment_date": {
              "date": "2020-09-29T00:00:00.000Z"
            },
            "closed_date": {
              "date": "2020-10-29T00:00:00.000Z"
            },
            "report_date": {
              "date": "2020-10-31T00:00:00.000Z"
            },
            "high_credit": 67132,
            "current_balance": 0,
            "payment_history1": "000000000010000000000000",
            "payment_history2": "000000000010000000000000",
            "payment_history_start_date": {
              "date": "2020-10-01T00:00:00.000Z"
            },
            "payment_history_end_date": {
              "date": "2020-03-01T00:00:00.000Z"
            },
            "repayment_months": 4,
            "emi_amount": 19250,
            "payment_frequency": "03",
            "actual_payment_amount": 67132,
            "dpd": {}
          }
        ],
        "user_enquiries": [
          {
            "_id": {
              "oid": "60549596af82eb0a0efb41a7"
            },
            "_type": "UserEnquiry",
            "capture_date": {
              "date": "2021-03-19T00:00:00.000Z"
            },
            "source": "cibil",
            "report_date": {
              "date": "2018-08-16T00:00:00.000Z"
            },
            "enquirer_name": "NOT DISCLOSED",
            "enquiry_purpose_code": "10",
            "enquiry_amount": 10000
          }
        ],
        "user_header_details": [
          {
            "_id": {
              "oid": "60549596af82eb0a0efb41ae"
            },
            "_type": "UserHeaderDetail",
            "capture_date": {
              "date": "2021-03-19T00:00:00.000Z"
            },
            "source": "cibil",
            "member_id": "NB49628899",
            "member_reference_id": "50982",
            "control_number": "003802469153",
            "date_processd": {
              "date": "2021-03-19T00:00:00.000Z"
            },
            "time_processd": {
              "date": "2021-03-19T12:14:44.000Z"
            }
          }
        ],
        "lender_id": 17,
        "control_number": "003802469153",
        "company_id": 18663,
        "loan_application_id": 50982
      },
      "bankstatment": {
        "customerInfo": {
          "name": "GANESH TRADING COMPANY",
          "address": "KHAWET NO 489 KHATA NUMBER 933 VPO CHAUDHARIWAS DIST-HISAR HISAR HR 125001",
          "landline": "",
          "mobile": "",
          "email": "",
          "pan": "",
          "perfiosTransactionId": "N7981604646556183",
          "customerTransactionId": "47318",
          "bank": "Bandhan Bank, India",
          "instId": 156
        },
        "statementdetails": [
          {
            "fileName": "company12859APRIL2020BANDHANBANK.pdf",
            "statementStatus": "VERIFIED",
            "customerInfo": {
              "name": "GANESH TRADING COMPANY",
              "address": "KHAWET NO 489 KHATA NUMBER 933 VPO CHAUDHARIWAS DIST-HISAR HISAR HR 125001",
              "landline": "",
              "mobile": "",
              "email": "",
              "pan": "",
              "bank": "Bandhan Bank, India"
            },
            "statementAccounts": [
              {
                "accountNo": "10180007166968",
                "accountType": "Bank",
                "xnsStartDate": "2020-04-03",
                "xnsEndDate": "2020-04-30"
              }
            ]
          }
        ],
        "accountAnalysis": [
          {
            "accountNo": "10180007166968",
            "accountType": "CURRENT",
            "loanTrackDetails": [
              {
                "amount": 212,
                "category": "Loan",
                "dates": "27-Apr-20 "
              }
            ],
            "summaryInfo": {
              "instName": "Bandhan Bank, India",
              "accNo": "10180007166968",
              "accType": "CURRENT",
              "fullMonthCount": 7,
              "total": {
                "allPenalCharges": 50,
                "bal1": 1712066.86,
                "bal10": 699836.86,
                "bal15": 865567.86,
                "bal20": 380531.86,
                "bal25": 403302.82,
                "bal5": 753193.86,
                "balAvg": 812120.83,
                "balAvgNeg": 0,
                "balLast": 756346.68,
                "balMax": 2994031.86,
                "balMin": 59001.08,
                "bouncedOrPenals": 2,
                "cashDeposits": 32,
                "cashWithdrawals": 5,
                "chqDeposits": 52,
                "chqIssues": 9,
                "clearedInwChqBounces": 0,
                "credits": 184,
                "creditsAPS": 189,
                "creditsSC": 0,
                "creditsSelf": 0,
                "debits": 206,
                "debitsAPS": 211,
                "debitsSC": 0,
                "debitsSelf": 0,
                "dlodPrinPayDelay": 0,
                "dpLimit": 0,
                "emiEcsIssues": 6,
                "emiEcsLoanIssues": 6,
                "intPayDelay": 0,
                "invExpenses": 0,
                "invIncomes": 0,
                "inwBounces": 0,
                "inwChqBounceNonTechnical": 0,
                "inwChqBounces": 0,
                "inwChqBounceTechnical": 0,
                "loanDisbursals": 0,
                "maxInvExpense": 0,
                "maxInvIncome": 0,
                "outwBounces": 2,
                "outwChqBounces": 2,
                "overdrawnAmount": 0,
                "overdrawnAmountPeak": 0,
                "overdrawnDays": 0,
                "overdrawnDaysPeak": 0,
                "overdrawnInstances": 0,
                "penalCharges": 0,
                "salaries": 0,
                "snLimit": 0,
                "totalAllPenalCharge": -5716.18,
                "totalBelowMinBalPenalty": 0,
                "totalCashDeposit": 5059500,
                "totalCashWithdrawal": 1163000,
                "totalChqDeposit": 1103998,
                "totalChqIssue": 2525875,
                "totalClearedInwChqBounce": 0,
                "totalCredit": 14329800,
                "totalCreditAPS": 14410806,
                "totalCreditSC": 0,
                "totalCreditSelf": 0,
                "totalDebit": 15331091.18,
                "totalDebitAPS": 15412097.18,
                "totalDebitSC": 0,
                "totalDebitSelf": 0,
                "totalEmiEcsLoanIssue": 15540,
                "totalInterestCharged": 0,
                "totalInvExpense": 0,
                "totalInvIncome": 0,
                "totalInwBounce": 0,
                "totalInwChqBounce": 0,
                "totalInwChqBounceNonTechnical": 0,
                "totalInwChqBounceTechnical": 0,
                "totalLoanDisbursal": 0,
                "totalMaxCreditValue": 2788500,
                "totalMaxDebitValue": 3048677,
                "totalMinCreditValue": 24734,
                "totalMinDebitValue": 245,
                "totalOutwBounce": 21000,
                "totalOutwChqBounce": 21000,
                "totalPenalCharge": 0,
                "totalSalary": 0,
                "totalTaxPayment": 0
              },
              "average": {
                "allPenalCharges": 7,
                "bal1": 244580.98,
                "bal10": 99976.69,
                "bal15": 123652.55,
                "bal20": 54361.69,
                "bal25": 57614.69,
                "bal5": 107599.12,
                "balAvg": 116017.26,
                "balAvgNeg": 0,
                "balLast": 108049.53,
                "balMax": 427718.84,
                "balMin": 8428.73,
                "bouncedOrPenals": 0,
                "cashDeposits": 5,
                "cashWithdrawals": 1,
                "chqDeposits": 7,
                "chqIssues": 1,
                "clearedInwChqBounces": 0,
                "credits": 26,
                "creditsAPS": 27,
                "creditsSC": 0,
                "creditsSelf": 0,
                "debits": 29,
                "debitsAPS": 30,
                "debitsSC": 0,
                "debitsSelf": 0,
                "dlodPrinPayDelay": 0,
                "dpLimit": 0,
                "emiEcsIssues": 1,
                "emiEcsLoanIssues": 1,
                "intPayDelay": 0,
                "invExpenses": 0,
                "invIncomes": 0,
                "inwBounces": 0,
                "inwChqBounceNonTechnical": 0,
                "inwChqBounces": 0,
                "inwChqBounceTechnical": 0,
                "loanDisbursals": 0,
                "maxInvExpense": 0,
                "maxInvIncome": 0,
                "outwBounces": 0,
                "outwChqBounces": 0,
                "overdrawnAmount": 0,
                "overdrawnAmountPeak": 0,
                "overdrawnDays": 0,
                "overdrawnDaysPeak": 0,
                "overdrawnInstances": 0,
                "penalCharges": 0,
                "salaries": 0,
                "snLimit": 0,
                "totalAllPenalCharge": -816.6,
                "totalBelowMinBalPenalty": 0,
                "totalCashDeposit": 722785.71,
                "totalCashWithdrawal": 166142.86,
                "totalChqDeposit": 157714,
                "totalChqIssue": 360839.29,
                "totalClearedInwChqBounce": 0,
                "totalCredit": 2047114.29,
                "totalCreditAPS": 2058686.57,
                "totalCreditSC": 0,
                "totalCreditSelf": 0,
                "totalDebit": 2190155.88,
                "totalDebitAPS": 2201728.17,
                "totalDebitSC": 0,
                "totalDebitSelf": 0,
                "totalEmiEcsLoanIssue": 2220,
                "totalInterestCharged": 0,
                "totalInvExpense": 0,
                "totalInvIncome": 0,
                "totalInwBounce": 0,
                "totalInwChqBounce": 0,
                "totalInwChqBounceNonTechnical": 0,
                "totalInwChqBounceTechnical": 0,
                "totalLoanDisbursal": 0,
                "totalMaxCreditValue": 398357.14,
                "totalMaxDebitValue": 435525.29,
                "totalMinCreditValue": 3533.43,
                "totalMinDebitValue": 35,
                "totalOutwBounce": 3000,
                "totalOutwChqBounce": 3000,
                "totalPenalCharge": 0,
                "totalSalary": 0,
                "totalTaxPayment": 0
              }
            },
            "monthlyDetails": [
              {
                "allPenalCharges": 0,
                "bal1": 1152912.58,
                "bal10": 139912.58,
                "bal15": 392633.58,
                "bal20": 12633.58,
                "bal25": 12633.58,
                "bal5": 189912.58,
                "balAvg": 243982.95,
                "balAvgNeg": 0,
                "balLast": 34948.58,
                "balMax": 1152912.58,
                "balMin": 12633.58,
                "bouncedOrPenals": 0,
                "cashDeposits": 2,
                "cashWithdrawals": 1,
                "chqDeposits": 0,
                "chqIssues": 1,
                "clearedInwChqBounces": 0,
                "credits": 19,
                "creditsAPS": 19,
                "creditsSC": 0,
                "creditsSelf": 0,
                "debits": 16,
                "debitsAPS": 16,
                "debitsSC": 0,
                "debitsSelf": 0,
                "dlodPrinPayDelay": 0,
                "dpLimit": 0,
                "emiEcsIssues": 2,
                "emiEcsLoanIssues": 2,
                "intPayDelay": 0,
                "invExpenses": 0,
                "invIncomes": 0,
                "inwBounces": 0,
                "inwChqBounceNonTechnical": 0,
                "inwChqBounces": 0,
                "inwChqBounceTechnical": 0,
                "loanDisbursals": 0,
                "maxInvExpense": 0,
                "maxInvIncome": 0,
                "monthName": "Apr-20",
                "outwBounces": 0,
                "outwChqBounces": 0,
                "overdrawnAmount": 0,
                "overdrawnAmountPeak": 0,
                "overdrawnDays": 0,
                "overdrawnDaysPeak": 0,
                "overdrawnInstances": 0,
                "penalCharges": 0,
                "salaries": 0,
                "snLimit": 0,
                "startDate": "2020-04-01",
                "totalAllPenalCharge": 0,
                "totalBelowMinBalPenalty": 0,
                "totalCashDeposit": 290000,
                "totalCashWithdrawal": 963000,
                "totalChqDeposit": 0,
                "totalChqIssue": 963000,
                "totalClearedInwChqBounce": 0,
                "totalCredit": 1785580,
                "totalCreditAPS": 1785580,
                "totalCreditSC": 0,
                "totalCreditSelf": 0,
                "totalDebit": 2903544,
                "totalDebitAPS": 2903544,
                "totalDebitSC": 0,
                "totalDebitSelf": 0,
                "totalEmiEcsLoanIssue": 3291,
                "totalInterestCharged": 0,
                "totalInvExpense": 0,
                "totalInvIncome": 0,
                "totalInwBounce": 0,
                "totalInwChqBounce": 0,
                "totalInwChqBounceNonTechnical": 0,
                "totalInwChqBounceTechnical": 0,
                "totalLoanDisbursal": 0,
                "totalMaxCreditValue": 237500,
                "totalMaxDebitValue": 963000,
                "totalMinCreditValue": 10000,
                "totalMinDebitValue": 212,
                "totalOutwBounce": 0,
                "totalOutwChqBounce": 0,
                "totalPenalCharge": 0,
                "totalSalary": 0,
                "totalTaxPayment": 0
              }
            ],
            "eODBalances": [
              {
                "date": "2020-04-01",
                "balance": 1152912.58
              },
              {
                "date": "2020-10-31",
                "balance": 151621.4
              }
            ],
            "top5FundsReceived": [
              {
                "month": "Apr-20",
                "category": "Transfer from VAKIL SINGH",
                "amount": 237500
              },
              {
                "month": "Oct-20",
                "category": "Transfer from AJIT",
                "amount": 180000
              }
            ],
            "top5FundsTransferred": [
              {
                "month": "Apr-20",
                "category": "Transfer to MS VINDHYA INDUSTRIES",
                "amount": 1300000
              },
              {
                "month": "Oct-20",
                "category": "Transfer to ROHIT WRAPERS",
                "amount": 550000
              },
              {
                "month": "Oct-20",
                "category": "Transfer to Suresh kumar and sons",
                "amount": 250000
              }
            ],
            "chqDebitXns": [
              {
                "date": "2020-04-03",
                "chqNo": "22",
                "narration": "WTHDRL",
                "amount": -963000,
                "category": "Cash Withdrawal",
                "balance": 189912.58
              },
              {
                "date": "2020-08-25",
                "chqNo": "27",
                "narration": "WTHDRL",
                "amount": -80000,
                "category": "Cash Withdrawal",
                "balance": 191012.88
              },
              {
                "date": "2020-10-07",
                "chqNo": "29",
                "narration": "WTHDRL,CLG/000029/JINDAL SUPREME INDIA PR",
                "amount": -199198,
                "category": "Transfer to JINDAL SUPREME INDIA PR",
                "balance": 124249.18
              }
            ],
            "fCUAnalysis": {
              "possibleFraudIndicators": {
                "suspiciousBankEStatements": {
                  "status": "false"
                }
              },
              "behaviouralTransactionalIndicators": {
                "equalCreditDebitXns": {
                  "status": "false"
                },
                "irregularTransferToPartiesXns": [
                  {
                    "group": 1,
                    "date": "2020-06-29",
                    "chqNo": "",
                    "narration": "WITHDRAWAL,WDL-IMPS/018116007444/Ajay trading co/KKBK0004333/XXXXXX7319/Aj ay Trading",
                    "amount": -50000,
                    "category": "Transfer to AJAY TRADING CO",
                    "balance": 87670.88
                  },
                  {
                    "group": 9,
                    "date": "2020-10-07",
                    "chqNo": "",
                    "narration": "WITHDRAWAL,WDL-IMPS/028115010374/SUSHANT GARG/HDFC0000155/XXXXXXXXXX5749/Sushant",
                    "amount": -10000,
                    "category": "Transfer to SUSHANT GARG",
                    "balance": 164249.18
                  }
                ]
              }
            }
          }
        ],
        "combinedAccountXns": [
          {
            "slNo": 1,
            "date": "2020-04-03",
            "chqNo": "22",
            "narration": "WTHDRL",
            "amount": -963000,
            "category": "Cash Withdrawal",
            "balance": 189912.58,
            "bank": "Bandhan Bank, India",
            "accNo": "10180007166968"
          }
        ],
        "combinedMonthlyDetails": [
          {
            "monthName": "Apr-20",
            "startDate": "2020-04-01"
          }
        ],
        "combinedBouncedOrPenalXns": [
          {
            "slNo": 1,
            "date": "2020-09-15",
            "chqNo": "",
            "narration": "WTHDRL,RTN/CLG/239964/Funds Insufficient/PUNJAB NATIONAL BANK",
            "amount": -14000,
            "category": "Bounced O/W Cheque",
            "balance": 150479.88,
            "bank": "Bandhan Bank, India",
            "accNo": "10180007166968"
          }
        ],
        "combinedAllPenalChargesXns": [
          {
            "slNo": 1,
            "date": "2020-05-28",
            "chqNo": "",
            "narration": "FEE CHG,IMPS transaction fee 014910001763",
            "amount": -6,
            "category": "Bank Charges",
            "balance": 92074.58,
            "bank": "Bandhan Bank, India",
            "accNo": "10180007166968"
          }
        ],
        "combinedEmiEcsLoanXns": [
          {
            "slNo": 1,
            "date": "2020-04-13",
            "chqNo": "",
            "narration": "WITHDRAWAL,ACH Debit-MINTIFI FINSERVE PVT-BDBL0000000000967916-40272-7059116881",
            "amount": -3079,
            "category": "Loan",
            "balance": 266633.58,
            "bank": "Bandhan Bank, India",
            "accNo": "10180007166968"
          }
        ],
        "combinedHolidayXns": [
          {
            "slNo": 1,
            "date": "2020-04-10",
            "chqNo": "",
            "narration": "WITHDRAWAL,WDL-IMPS/010120005074/SHALIMAR PAINTS LTD/SBIN0004732/XXXXXXX5596 /Shalimar",
            "amount": -50000,
            "category": "Transfer to SHALIMAR PAINTS Ltd",
            "balance": 139912.58,
            "bank": "Bandhan Bank, India",
            "accNo": "10180007166968"
          }
        ],
        "combinedRegularDebitXns": [
          {
            "groupNo": 1,
            "slNo": 1,
            "date": "2020-06-02",
            "chqNo": "",
            "narration": "WITHDRAWAL,WDL-IMPS/015412005227/Mintifi/IDFB0040102/XXXXXXXX0272/Mintifi",
            "amount": -50000,
            "category": "Transfer to MINTIFI",
            "balance": 112561.88,
            "bank": "Bandhan Bank, India",
            "accNo": "10180007166968"
          }
        ],
        "accountXns": [
          {
            "accountNo": "10180007166968",
            "accountType": "CURRENT",
            "ifscCode": "BDBL0001826",
            "micrCode": "125750052",
            "location": "HISAR",
            "xns": [
              {
                "date": "2020-04-03",
                "chqNo": "22",
                "narration": "WTHDRL",
                "amount": -963000,
                "category": "Cash Withdrawal",
                "balance": 189912.58
              }
            ]
          }
        ],
        "AdditionalMonthlyDetails": {
          "MonthlyData1": [
            {
              "monthName": "Apr-20",
              "credits": 19,
              "debits": 14,
              "totalCredit": 1785580,
              "totalDebit": 2900253,
              "overdrawnAmountPeak": 0,
              "overdrawnAverage": 0,
              "limitUtilization": 0,
              "peakUtilization": 0,
              "balAvgfor10th20thlast": 62498.25,
              "overdrawnAveragePercent": 0,
              "interestOnAvgEOD": 0,
              "debitSummationPercent": 0,
              "inWardPaymentReturn": 0,
              "outWardPaymentReturn": 0,
              "numberOfTransactions": 35,
              "balAvgOf6Dates": 316773.08,
              "creditSummation": 1785580,
              "creditSummationPercent": 0,
              "subLimitUtilisation": 0,
              "inwChqReturnsPercent": 0,
              "outwChqReturnsPercent": 0,
              "netBusinessCredit": 1785580
            }
          ]
        },
        "AdditionalSummaryInfo": [
          {
            "productType": "",
            "repaymentAccount": "YES",
            "maxPeakDelayPrincipal": "NA",
            "maxPeakDelayInterestDLOD": "NA",
            "maxPeakDelayInterestCC": "NA"
          }
        ]
      }
    }
  }
})
headers = {
  'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
  'sec-ch-ua-mobile': '?0',
  'Authorization': 'Bearer H9KDSeRqG6DBaz-RAV2lxI9DmBIW0dNfzXiOWQMiOSkpMnl8vJ6yRmJPapJbGfdAnvfj_LN1m5pvDKV_zu6wdQ==',
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Referer': 'http://localhost:8080/',
  'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
  'sec-ch-ua-platform': '"Linux"'
}

for i in range(0,5000):
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
