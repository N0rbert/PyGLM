#pragma once

#include "../../compiler_setup.h"

#include "../../types/all.h"

template<int L, typename T>
static constexpr PyTypeObject* PyGLM_VEC_TYPE() {
	return (std::is_same<vec<L, T>, vec<1, float> >::value) ? (PyTypeObject*)&hfvec1Type :
		(std::is_same<vec<L, T>, vec<2, float> >::value) ? (PyTypeObject*)&hfvec2Type :
		(std::is_same<vec<L, T>, vec<3, float> >::value) ? (PyTypeObject*)&hfvec3Type :
		(std::is_same<vec<L, T>, vec<4, float> >::value) ? (PyTypeObject*)&hfvec4Type :
		(std::is_same<vec<L, T>, vec<1, double> >::value) ? (PyTypeObject*)&hdvec1Type :
		(std::is_same<vec<L, T>, vec<2, double> >::value) ? (PyTypeObject*)&hdvec2Type :
		(std::is_same<vec<L, T>, vec<3, double> >::value) ? (PyTypeObject*)&hdvec3Type :
		(std::is_same<vec<L, T>, vec<4, double> >::value) ? (PyTypeObject*)&hdvec4Type :
		(std::is_same<vec<L, T>, vec<1, int8> >::value) ? (PyTypeObject*)&hi8vec1Type :
		(std::is_same<vec<L, T>, vec<2, int8> >::value) ? (PyTypeObject*)&hi8vec2Type :
		(std::is_same<vec<L, T>, vec<3, int8> >::value) ? (PyTypeObject*)&hi8vec3Type :
		(std::is_same<vec<L, T>, vec<4, int8> >::value) ? (PyTypeObject*)&hi8vec4Type :
		(std::is_same<vec<L, T>, vec<1, int16> >::value) ? (PyTypeObject*)&hi16vec1Type :
		(std::is_same<vec<L, T>, vec<2, int16> >::value) ? (PyTypeObject*)&hi16vec2Type :
		(std::is_same<vec<L, T>, vec<3, int16> >::value) ? (PyTypeObject*)&hi16vec3Type :
		(std::is_same<vec<L, T>, vec<4, int16> >::value) ? (PyTypeObject*)&hi16vec4Type :
		(std::is_same<vec<L, T>, vec<1, int32> >::value) ? (PyTypeObject*)&hivec1Type :
		(std::is_same<vec<L, T>, vec<2, int32> >::value) ? (PyTypeObject*)&hivec2Type :
		(std::is_same<vec<L, T>, vec<3, int32> >::value) ? (PyTypeObject*)&hivec3Type :
		(std::is_same<vec<L, T>, vec<4, int32> >::value) ? (PyTypeObject*)&hivec4Type :
		(std::is_same<vec<L, T>, vec<1, int64> >::value) ? (PyTypeObject*)&hi64vec1Type :
		(std::is_same<vec<L, T>, vec<2, int64> >::value) ? (PyTypeObject*)&hi64vec2Type :
		(std::is_same<vec<L, T>, vec<3, int64> >::value) ? (PyTypeObject*)&hi64vec3Type :
		(std::is_same<vec<L, T>, vec<4, int64> >::value) ? (PyTypeObject*)&hi64vec4Type :
		(std::is_same<vec<L, T>, vec<1, uint8> >::value) ? (PyTypeObject*)&hu8vec1Type :
		(std::is_same<vec<L, T>, vec<2, uint8> >::value) ? (PyTypeObject*)&hu8vec2Type :
		(std::is_same<vec<L, T>, vec<3, uint8> >::value) ? (PyTypeObject*)&hu8vec3Type :
		(std::is_same<vec<L, T>, vec<4, uint8> >::value) ? (PyTypeObject*)&hu8vec4Type :
		(std::is_same<vec<L, T>, vec<1, uint16> >::value) ? (PyTypeObject*)&hu16vec1Type :
		(std::is_same<vec<L, T>, vec<2, uint16> >::value) ? (PyTypeObject*)&hu16vec2Type :
		(std::is_same<vec<L, T>, vec<3, uint16> >::value) ? (PyTypeObject*)&hu16vec3Type :
		(std::is_same<vec<L, T>, vec<4, uint16> >::value) ? (PyTypeObject*)&hu16vec4Type :
		(std::is_same<vec<L, T>, vec<1, uint32> >::value) ? (PyTypeObject*)&huvec1Type :
		(std::is_same<vec<L, T>, vec<2, uint32> >::value) ? (PyTypeObject*)&huvec2Type :
		(std::is_same<vec<L, T>, vec<3, uint32> >::value) ? (PyTypeObject*)&huvec3Type :
		(std::is_same<vec<L, T>, vec<4, uint32> >::value) ? (PyTypeObject*)&huvec4Type :
		(std::is_same<vec<L, T>, vec<1, uint64> >::value) ? (PyTypeObject*)&hu64vec1Type :
		(std::is_same<vec<L, T>, vec<2, uint64> >::value) ? (PyTypeObject*)&hu64vec2Type :
		(std::is_same<vec<L, T>, vec<3, uint64> >::value) ? (PyTypeObject*)&hu64vec3Type :
		(std::is_same<vec<L, T>, vec<4, uint64> >::value) ? (PyTypeObject*)&hu64vec4Type :
		(std::is_same<vec<L, T>, vec<1, bool> >::value) ? (PyTypeObject*)&hbvec1Type :
		(std::is_same<vec<L, T>, vec<2, bool> >::value) ? (PyTypeObject*)&hbvec2Type :
		(std::is_same<vec<L, T>, vec<3, bool> >::value) ? (PyTypeObject*)&hbvec3Type :
		(std::is_same<vec<L, T>, vec<4, bool> >::value) ? (PyTypeObject*)&hbvec4Type :
		(PyTypeObject*)0;
}