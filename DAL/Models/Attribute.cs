namespace UIMS.Api.DAL.Models;

public class Attribute
{
    public virtual int Id { get; set; }
    public virtual string? Name { get; set; }
    public virtual ICollection<Item>? Items { get; set; }
}