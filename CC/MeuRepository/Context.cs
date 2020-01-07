using Banco.Domain;
using Microsoft.EntityFrameworkCore;
using System;
using System.Collections.Generic;
using System.Text;
using WebApi.Entities;
using Banco.Domain.Entities;

namespace Banco.Repository
{
    public class Context: DbContext
    {
        public Context(DbContextOptions<Context> options) : base(options) { }
        public virtual DbSet<User> Users { get; set; }
        public virtual DbSet<ContaCorrente> ContasCorrente { get; set; }


        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            base.OnModelCreating(modelBuilder);
            
           
        }        
    }
}
