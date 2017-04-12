namespace Yamaha.Business.Model.Warranty.Owner
{
    public class Individual : OwnerDetail
    {
        public string IdNumber { get; set; }
        public string Surname { get; set; }
        public string FirstName { get; set; }
        public string Title { get; set; }
        public string Occupation { get; set; }
        public AgeGroup AgeGroup { get; set; }
    }
}
