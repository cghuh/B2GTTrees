#ifndef Fireworks_Core_FWSimpleRepresentationChecker_h
#define Fireworks_Core_FWSimpleRepresentationChecker_h
// -*- C++ -*-
//
// Package:     Core
// Class  :     FWSimpleRepresentationChecker
//
/**\class FWSimpleRepresentationChecker FWSimpleRepresentationChecker.h Fireworks/Core/interface/FWSimpleRepresentationChecker.h

   Description: Used to check to see if a Simple proxy builder could be used to represent a particular type

   Usage:
    <usage>

 */
//
// Original Author:  Chris Jones
//         Created:  Tue Nov 25 10:54:22 EST 2008
// $Id: FWSimpleRepresentationChecker.h,v 1.1 2008/11/26 01:52:31 chrjones Exp $
//

// system include files
#include "Reflex/Type.h"

// user include files
#include "Fireworks/Core/interface/FWRepresentationCheckerBase.h"

// forward declarations

class FWSimpleRepresentationChecker : public FWRepresentationCheckerBase {

public:
   FWSimpleRepresentationChecker(const std::string& iTypeName,
                                 const std::string& iPurpose);
   virtual ~FWSimpleRepresentationChecker();

   // ---------- const member functions ---------------------
   virtual FWRepresentationInfo infoFor(const std::string& iTypeName) const;

   // ---------- static member functions --------------------

   // ---------- member functions ---------------------------

private:
   FWSimpleRepresentationChecker(const FWSimpleRepresentationChecker&); // stop default

   const FWSimpleRepresentationChecker& operator=(const FWSimpleRepresentationChecker&); // stop default

   // ---------- member data --------------------------------
   ROOT::Reflex::Type m_type;
};


#endif
