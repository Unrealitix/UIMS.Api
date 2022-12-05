namespace UIMS.Api.DAL.Models;

public class Group
{
    public virtual int? Id { get; set; }
    public virtual string? Name { get; set; }
    public virtual ICollection<Item>? Items { get; set; }
}