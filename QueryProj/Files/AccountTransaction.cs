//#PK=PaymentDate,Reference
//#MD=12

using System;
using System.Collections.Generic;
using System.Linq;

namespace Yamaha.Business.Model.Accounts
{
    public class AccountTransaction
    {
        public AccountTransaction()
        {
            Payments = new List<AccountPayment>();
        }
        public string DocumentNumber { get; set; }
        public DocumentType DocumentType { get; set; }
        public DateTime TransactionDate { get; set; }
        public string Reference { get; set; }
        public decimal Backorder { get; set; }
        public DateTime DueDate { get; set; }
        public decimal DebitBalance { get; set; }
        public decimal CreditBalance { get; set; }
        public decimal Balance { get; set; }
        public string CustomerPurchaseOrder { get; set; }
        public decimal InvoiceValue { get; set; }
        public string EsaValue { get; set; }
        public DateTime EsaDate { get; set; }

        public IList<AccountPayment> Payments { get; set; }
    }
}