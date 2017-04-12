using System;
using System.Collections.Generic;
using Yamaha.Business.Model.Branches;

namespace Yamaha.Business.Model.Accounts
{
    public class AccountQuery
    {
        public CustomerAccount CustomerAccount { get; set; }
        public CustomerSubaccount CustomerSubaccount { get; set; }
        public Branch Branch { get; set; }
        public string Address1 { get; set; }
        public string Address2 { get; set; }
        public string Address3 { get; set; }
        public DateTime LastPaymentDate { get; set; }
        public bool OverLimit
        {
            get
            {
                if (CreditLimit == 0)
                    return false;

                return (CreditLimit - TotalOwingBalance - TotalNotInvoiced < 0);
            }
        }
        public decimal Current { get; set; }
        public decimal ThirtyDays { get; set; }
        public decimal SixtyDays { get; set; }
        public decimal NinetyDays { get; set; }
        public decimal HundredTwentyDays { get; set; }
        public decimal TotalNotInvoiced { get; set; }
        public decimal TotalOwingBalance { get; set; }
        public decimal CreditLimit { get; set; }
        public decimal SalesOrdersPendingSubmission { get; set; }
        public IList<AccountTransaction> Transactions { get; set; }
        public IList<AccountCheque> Cheques { get; set; }
        public IList<AccountCheque> PostdatedCheques { get; set; }
    }
}