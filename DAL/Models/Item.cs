using System.ComponentModel.DataAnnotations;
using Microsoft.EntityFrameworkCore;

namespace UIMS.Api.DAL.Models;

public class Item
{
    [Key]
    public virtual string? Sku { get; set; }
    public virtual string? Barcode { get; set; }
    public virtual string? Name { get; set; }
    public virtual int? GroupId { get; set; }
    public virtual Group? Group { get; set; }
    public virtual string? Description { get; set; }
    public virtual int? Quantity { get; set; }
    public virtual string? Supplier { get; set; }
    public virtual ICollection<ItemAttribute>? Attributes { get; set; }
    public virtual DateTime CreatedOn { get; set; } = DateTime.UtcNow;
}