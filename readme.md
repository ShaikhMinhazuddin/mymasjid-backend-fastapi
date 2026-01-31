Admin Database {
    adminid : randomly generated
    name : Full Name
    masjidID : IAJM769003
    admin_contact : phno
    password : UniquePassword with min 8 character
}

Masjid Database {
    masjidId : First Character of Name words + pincode
    masjid_name : Ispat Anjuman Jama Masjid
    address : Sector-15, Rourkela,
    latitude : ,
    longitude : ,
    pin : 769003
    adminid : admin database
}

Notification  {
    notificationId: unique
    notificationSubject : Headline
    notificationType : Community Annoucement / Masjid Annoucement
    notification Details : If any,
    additional Links : If any
}

prayertimes{
    masjidId:
    fajr_adhan_time:
    fajr_jamat_time:
    zuhr_adhan_time:
    zuhr_jamat_time:
    asr_adhan_time:
    asr_jamat_time:
    magrib_adhan_time:
    magrib_jamat_time:
    isha_adhan_time:
    isha_jamat_time:
}

And the other calculation will be done through the Internet