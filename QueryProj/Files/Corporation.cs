namespace Yamaha.Business.Model.Warranty.Owner
{
    public class Corporation : OwnerDetail
    {
        public string RegistrationNumber { get; set; }
        public string RegisteredName { get; set; }
        public string TradingName { get; set; }
        public string BranchName { get; set; }
        public CorporationType CorporationType { get; set; }
        public string BusinessActivity { get; set; }
    }
}
