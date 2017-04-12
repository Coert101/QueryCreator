using System;
using Yamaha.Business.Model.Base;

namespace Yamaha.Business.Model.Warranty.Product
{
    public abstract class ProductDetail : BaseModel
    {
        public string WarrantyAccountNumber { get; set; }
        public string EngineSerialNumber { get; set; }

        public ProductDetailType ProductType
        {
            get
            {
                if (this.GetType() == typeof(GolfCarDetail))
                    return ProductDetailType.GolfCar;
                else if (this.GetType() == typeof(MarineDetail))
                    return ProductDetailType.Marine;
                else if (this.GetType() == typeof(MotorcycleDetail))
                    return ProductDetailType.Motorcycle;
                else if (this.GetType() == typeof(PowerDetail))
                    return ProductDetailType.PowerTool;
                else
                    throw new NotSupportedException("Unable to determine Product Detail Type");
            }
        }
    }
}
