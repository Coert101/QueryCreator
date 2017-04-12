using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Yamaha.Business.Model.Accounts
{
    public class AccountPayment
    {
        public string Invoice { get; set; }

        public string InvoiceType { get; set; }

        public string Reference { get; set; }

        public decimal TransactionValue { get; set; }

        public string PaymentJournal { get; set; }

        public DateTime JournalDate { get; set; }

        public decimal DiscountValue { get; set; }
    }
}
