namespace UIMS.Api.DAL.Models;

public class ItemAttribute
{
    public virtual int Id { get; set; }
    public virtual string ItemId { get; set; }
    public virtual Item Item { get; set; }
    public virtual string AttributeId { get; set; }
    public virtual Attribute Attribute { get; set; }
    public virtual string? Value { get; set; }
}