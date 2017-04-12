using System.ComponentModel.DataAnnotations;

namespace Yamaha.Business.Model.Branches
{
    public class Branch
    {
        public Branch(string branchCode) : this() { BranchCode = branchCode; }
        public Branch()
        {
            AllowMerchandiseAccountQuery = false;
            AllowSalesOrders = false;
            AllowSalesOrders = false;
        }

        public string BranchCode { get; set; }
        [Required]
        public bool AllowSalesOrders { get; set; }
        [Required]
        public bool AllowMerchandiseAccountQuery { get; set; }
        [Required]
        public bool AllowUnitAccountQuery { get; set; }
    }
}
