using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Yamaha.Business.Model.Accounts
{
    public class CreditLimitCheck
    {
        public bool CreditLimitExceeded { get; set; }
        public string Message { get; set; }
    }
}
