using Microsoft.EntityFrameworkCore;
using UIMS.Api.DAL.Models;
using Attribute = UIMS.Api.DAL.Models.Attribute;

namespace UIMS.Api.DAL;

public class DataContext : DbContext
{
    public DataContext(DbContextOptions<DataContext> options) : base(options) {}

    public DbSet<Group> Groups { get; set; } = null;
    public DbSet<Item> Items { get; set; } = null;
    public DbSet<Attribute> Attributes { get; set; } = null;

    // protected override void OnModelCreating(ModelBuilder modelBuilder)
    // {
    //     modelBuilder.Entity<Group>()
    //         .HasMany(a => a.Items)
    //         .WithOne();
    // }
}