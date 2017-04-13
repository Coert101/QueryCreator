//#PK=PaymentDate,Reference
//#MD=5

using System;

namespace Yamaha.Business.Model.Accounts
{
    public class AccountCheque
    {
        public DateTime PaymentDate { get; set; }
		//#MAXLENGTH=50
        public string Reference { get; set; }
        public decimal Value { get; set; }
    }
}