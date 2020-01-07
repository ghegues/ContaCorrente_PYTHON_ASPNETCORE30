using AutoMapper;
using Banco.Domain;
using WebApi.Entities;
using WebApi.Models.Users;

namespace WebApi.Helpers
{
    public class AutoMapperProfile : Profile
    {
        public AutoMapperProfile()
        {
            CreateMap<User, UserModel>();
            CreateMap<RegisterModel, User>();
            CreateMap<UpdateModel, User>();

        }
    }
}